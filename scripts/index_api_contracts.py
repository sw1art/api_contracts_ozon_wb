# /// script
# requires-python = ">=3.12"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Build an offline route inventory from saved official marketplace documentation.

Run: uv run scripts/index_api_contracts.py [--check]
This script makes no network requests and never needs seller credentials.
"""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "docs" / "api-contracts"
METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}


class ContractLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently losing published paths or methods."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate YAML key in official specification")
        return super().construct_mapping(node, deep=deep)


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def wb_operations():
    sources = json.loads((ROOT / "wb" / "sources.json").read_text(encoding="utf-8"))
    operations = []
    declared = {entry["file"] for entry in sources["specifications"]}
    actual = {path.name for path in (ROOT / "wb").glob("*.yaml")}
    if declared != actual:
        raise ValueError("WB specification inventory does not match saved YAML files")
    for source in sources["specifications"]:
        spec = yaml.load(
            (ROOT / "wb" / source["file"]).read_text(encoding="utf-8"), Loader=ContractLoader
        )
        if not str(spec.get("openapi", "")).startswith("3.") or not spec.get("paths"):
            raise ValueError(f"Invalid OpenAPI document: {source['file']}")
        for path, item in spec["paths"].items():
            if not path.startswith("/") or "$ref" in item:
                raise ValueError(f"Unsupported path entry: {source['file']} {path}")
            for method, operation in item.items():
                if method not in METHODS:
                    continue
                servers = operation.get("servers", item.get("servers", spec.get("servers", [])))
                operations.append(
                    {
                        "method": method.upper(),
                        "path": path,
                        "servers": servers,
                        "operation_id": operation.get("operationId"),
                        "summary": operation.get("summary", ""),
                        "tags": operation.get("tags", []),
                        "deprecated": operation.get("deprecated", False),
                        "security": operation.get("security", spec.get("security", [])),
                        "section": source["section"],
                        "documentation": source["swagger"],
                        "source_file": "wb/" + source["file"],
                    }
                )
    return sources, operations


def validate_operations(operations):
    if not operations:
        raise ValueError("Empty operation inventory")
    for operation in operations:
        if operation.get("method", "").lower() not in METHODS:
            raise ValueError(f"Invalid HTTP method: {operation}")
        if not operation.get("path", "").startswith("/"):
            raise ValueError(f"Invalid HTTP path: {operation}")
        if not operation.get("documentation", "").startswith("https://"):
            raise ValueError(f"Missing documentation source: {operation}")


def markdown_cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def render():
    sources, wb = wb_operations()
    ozon_source = json.loads((ROOT / "ozon" / "operations.json").read_text(encoding="utf-8"))
    ozon = ozon_source["operations"]
    if sources["captured_on"] != ozon_source["captured_on"]:
        raise ValueError(
            "Marketplaces have different capture dates; review the snapshot explicitly"
        )
    for operations in (wb, ozon):
        validate_operations(operations)
    artifacts = {
        "wb/operations.json": json_text(
            {
                "captured_on": sources["captured_on"],
                "format": "openapi-derived-index",
                "source": sources["documentation"],
                "operations": wb,
            }
        )
    }
    csv_buffer = io.StringIO(newline="")
    columns = [
        "marketplace",
        "method",
        "path",
        "servers",
        "operation_id",
        "summary",
        "documentation",
    ]
    writer = csv.DictWriter(csv_buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    markdown = [
        "# Полный индекс опубликованных методов WB и Ozon",
        "",
        f"Снимок: {sources['captured_on']}. Сгенерировано `scripts/index_api_contracts.py`.",
        "",
        "Это перечень из документации, а не список реализованных интеграций или проверенных прав.",
        "Старые/устаревшие и бета-методы сохраняются, если они присутствуют в источнике.",
        "",
    ]
    for marketplace, operations in (("wb", wb), ("ozon", ozon)):
        distinct = len({(op["method"], op["path"]) for op in operations})
        markdown += [
            f"## {marketplace.upper()}",
            "",
            f"Операций в документации: {len(operations)}; уникальных пар метод/путь: {distinct}.",
            "",
            "| Метод | Путь | Название | Источник |",
            "|---|---|---|---|",
        ]
        for operation in operations:
            servers = (
                [entry["url"] for entry in operation["servers"]]
                if marketplace == "wb"
                else [ozon_source["base_url"]]
            )
            writer.writerow(
                {
                    "marketplace": marketplace,
                    "method": operation["method"],
                    "path": operation["path"],
                    "servers": " ".join(servers),
                    "operation_id": operation.get("operation_id") or "",
                    "summary": operation["summary"],
                    "documentation": operation["documentation"],
                }
            )
            markdown.append(
                f"| {operation['method']} | `{markdown_cell(operation['path'])}` | "
                f"{markdown_cell(operation['summary'])} | "
                f"[описание]({operation['documentation']}) |"
            )
        markdown.append("")
    artifacts["routes.csv"] = csv_buffer.getvalue()
    artifacts["routes.md"] = "\n".join(markdown)
    inputs = [
        *sorted((ROOT / "wb").glob("*.yaml")),
        ROOT / "wb" / "sources.json",
        ROOT / "wb" / "general-documentation.txt",
        ROOT / "ozon" / "operations.json",
        ROOT / "ozon" / "documentation.txt",
    ]
    files = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in inputs}
    files.update({name: value.encode("utf-8") for name, value in artifacts.items()})
    artifacts["manifest.json"] = json_text(
        {
            "captured_on": sources["captured_on"],
            "wb_specifications": len(sources["specifications"]),
            "wb_operations": len(wb),
            "ozon_operations": len(ozon),
            "files": [
                {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
                for name, data in sorted(files.items())
            ],
        }
    )
    return artifacts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    args = parser.parse_args()
    artifacts = render()
    mismatched = []
    for name, content in artifacts.items():
        path = ROOT / name
        expected = content.encode("utf-8")
        if args.check:
            if not path.exists() or path.read_bytes() != expected:
                mismatched.append(name)
        else:
            path.write_bytes(expected)
    if mismatched:
        raise SystemExit("Regenerate API inventory: " + ", ".join(mismatched))
    manifest = json.loads(artifacts["manifest.json"])
    print(
        f"{'Checked' if args.check else 'Generated'} API inventory: "
        f"WB {manifest['wb_operations']} operations / {manifest['wb_specifications']} specs; "
        f"Ozon {manifest['ozon_operations']} operations"
    )


if __name__ == "__main__":
    main()
