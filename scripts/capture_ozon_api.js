/**
 * Read-only extraction for the fully rendered official Seller API documentation.
 * Evaluate this function in the documentation tab, then save the returned
 * `index` as ozon/operations.json and `documentationText` as ozon/documentation.txt.
 * This reads the DOM; it does not fetch API data or access seller credentials.
 */
function captureOzonApiSnapshot(capturedOn) {
  if (
    location.origin !== "https://docs.ozon.ru" ||
    location.pathname !== "/api/seller/"
  ) {
    throw new Error("Open the official Ozon Seller API documentation first");
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(capturedOn)) {
    throw new Error("Supply the snapshot date as YYYY-MM-DD");
  }
  const source = "https://docs.ozon.ru/api/seller/";
  const sections = [...document.querySelectorAll('[id^="operation/"]')];
  if (sections.length === 0) {
    throw new Error("Documentation has not loaded: no operation sections");
  }
  const operations = sections.map((section) => {
    const text = section.innerText;
    const route = text.match(/\n(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE)\n(\/[^\s]+)/);
    if (!route) {
      throw new Error(`Missing HTTP method or path: ${section.id}`);
    }
    return {
      method: route[1],
      path: route[2],
      operation_id: section.id.slice("operation/".length),
      summary: section.querySelector("h2")?.innerText || text.split("\n")[0],
      documentation: source + "#" + section.id,
    };
  });
  if (new Set(operations.map((entry) => entry.operation_id)).size !== operations.length) {
    throw new Error("Duplicate operation sections: inspect the rendered page");
  }
  return {
    index: {
      source,
      captured_on: capturedOn,
      format: "rendered-documentation-index",
      base_url: "https://api-seller.ozon.ru",
      operations,
    },
    documentationText: document.body.innerText,
  };
}
