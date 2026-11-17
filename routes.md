# Полный индекс опубликованных методов WB и Ozon

Снимок: 2026-11-17. Сгенерировано `scripts/index_api_contracts.py`.

Это перечень из документации, а не список реализованных интеграций или проверенных прав.
Старые/устаревшие и бета-методы сохраняются, если они присутствуют в источнике.

## WB

Операций в документации: 311; уникальных пар метод/путь: 311.

| Метод | Путь | Название | Источник |
|---|---|---|---|
| GET | `/ping` | Проверка подключения | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/communications/v2/news` | Получить новости портала продавцов | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/communications/v1/notifications` | Получить уведомления портала продавцов | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/v1/seller-info` | Получить информацию о продавце | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/common/v1/rating` | Получить рейтинг продавца | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/common/v1/subscriptions` | Получить информацию о подписке Джем | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/common/v1/tariff-constructor/options` | Получить информацию об опциях Конструктора тарифов | [описание](https://dev.wildberries.ru/swagger/general) |
| POST | `/api/v1/invite` | Создать приглашение для нового пользователя | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/api/v1/users` | Получить список активных или приглашённых пользователей продавца | [описание](https://dev.wildberries.ru/swagger/general) |
| PUT | `/api/v1/users/access` | Изменить права доступа пользователей | [описание](https://dev.wildberries.ru/swagger/general) |
| DELETE | `/api/v1/user` | Удалить пользователя | [описание](https://dev.wildberries.ru/swagger/general) |
| GET | `/content/v2/object/parent/all` | Родительские категории товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/object/all` | Список предметов | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/object/charcs/{subjectId}` | Характеристики предмета | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/colors` | Цвет | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/kinds` | Пол | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/countries` | Страна производства | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/seasons` | Сезон | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/vat` | Ставка НДС | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/directory/tnved` | Код ТН ВЭД предмета | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/content/v2/directory/tnved/all` | Список кодов ТН ВЭД | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/content/v2/directory/okpd` | Код ОКПД2 предмета | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/content/v2/directory/okpd/all` | Список кодов ОКПД2 | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/content/v1/brands` | Бренды | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/tags` | Список ярлыков | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/tag` | Создание ярлыка | [описание](https://dev.wildberries.ru/swagger/items) |
| PATCH | `/content/v2/tag/{id}` | Изменение ярлыка | [описание](https://dev.wildberries.ru/swagger/items) |
| DELETE | `/content/v2/tag/{id}` | Удаление ярлыка | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/tag/nomenclature/link` | Управление ярлыками в карточке товара | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/get/cards/list` | Список карточек товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/error/list` | Список несозданных карточек товаров с ошибками | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/update` | Редактирование карточек товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/moveNm` | Объединение и разъединение карточек товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/delete/trash` | Перенос карточек товаров в корзину | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/recover` | Восстановление карточек товаров из корзины | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/get/cards/trash` | Список карточек товаров в корзине | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/content/v2/cards/limits` | Лимиты карточек товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/barcodes` | Генерация баркодов | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/upload` | Создание карточек товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v2/cards/upload/add` | Создание карточек товаров с присоединением | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v3/media/file` | Загрузить медиафайл | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/content/v3/media/save` | Загрузить медиафайлы по ссылкам | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/content/v1/recommendations/list` | Список рекомендаций в карточках товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/content/v1/recommendations/set` | Установить рекомендации для товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v2/upload/task` | Установить цены и скидки | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v2/upload/task/size` | Установить цены для размеров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v2/upload/task/club-discount` | Установить скидки WB Клуба | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/discounts-prices/v1/upload/task/b2b/wholesale` | Установить оптовые скидки для B2B-продаж | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/history/tasks` | Состояние обработанной загрузки | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/history/goods/task` | Детализация обработанной загрузки | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/buffer/tasks` | Состояние необработанной загрузки | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/buffer/goods/task` | Детализация необработанной загрузки | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/list/goods/filter` | Получить товары с ценами | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v2/list/goods/filter` | Получить товары с ценами по артикулам | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/list/goods/size/nm` | Получить размеры товара с ценами | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v2/quarantine/goods` | Получить товары в карантине | [описание](https://dev.wildberries.ru/swagger/items) |
| PUT | `/api/v3/stocks/{warehouseId}` | Обновить остатки товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| DELETE | `/api/v3/stocks/{warehouseId}` | Удалить остатки товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v3/stocks/{warehouseId}` | Получить остатки товаров | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v3/offices` | Получить список складов WB | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v3/warehouses` | Получить список складов продавца | [описание](https://dev.wildberries.ru/swagger/items) |
| POST | `/api/v3/warehouses` | Создать склад продавца | [описание](https://dev.wildberries.ru/swagger/items) |
| PUT | `/api/v3/warehouses/{warehouseId}` | Обновить склад продавца | [описание](https://dev.wildberries.ru/swagger/items) |
| DELETE | `/api/v3/warehouses/{warehouseId}` | Удалить склад продавца | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Список контактов | [описание](https://dev.wildberries.ru/swagger/items) |
| PUT | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Обновить список контактов | [описание](https://dev.wildberries.ru/swagger/items) |
| GET | `/api/v3/passes/offices` | Получить список складов, для которых требуется пропуск | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/passes` | Получить список пропусков | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/passes` | Создать пропуск | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/passes/{passId}` | Обновить пропуск | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| DELETE | `/api/v3/passes/{passId}` | Удалить пропуск | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/orders/new` | Получить список новых сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/orders` | Получить информацию о сборочных заданиях | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/orders/status` | Получить статусы сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/supplies/orders/reshipment` | Получить все сборочные задания для повторной отгрузки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/v3/orders/{orderId}/cancel` | Отменить сборочное задание | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/orders/stickers` | Получить стикеры сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/orders/stickers/cross-border` | Получить стикеры сборочных заданий трансграничных поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/orders/status/history` | История статусов для сборочных заданий трансграничных поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/orders/client` | Заказы с информацией по клиенту | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/orders/archive` | Получить список архивных сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/marketplace/v3/orders/meta` | Получить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| DELETE | `/api/v3/orders/{orderId}/meta` | Удалить идентификаторы маркировки сборочного задания | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/orders/{orderId}/meta/sgtin` | Закрепить код маркировки Честного знака за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/orders/{orderId}/meta/uin` | Закрепить УИН за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/orders/{orderId}/meta/imei` | Закрепить IMEI за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/orders/{orderId}/meta/gtin` | Закрепить GTIN за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/v3/orders/{orderId}/meta/expiration` | Закрепить за сборочным заданием срок годности товара | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/marketplace/v3/orders/{orderId}/meta/customs-declaration` | Закрепить номер ДТ за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/supplies` | Создать новую поставку | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/supplies` | Получить список поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/marketplace/v3/supplies/{supplyId}/orders` | Добавить сборочные задания к поставке | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/marketplace/v3/fbs/supplies/{supplyId}/orders/transfer` | Перевести сборочные задания из доставки на сборку | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/supplies/{supplyId}` | Получить информацию о поставке | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| DELETE | `/api/v3/supplies/{supplyId}` | Удалить поставку | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/supplies/{supplyId}/order-ids` | Получить ID сборочных заданий поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/supplies/{supplyId}/shipping-points` | Получить список пунктов отгрузки поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/shipping-points` | Получить список пунктов отгрузки поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/marketplace/v3/fbs/supplies/shipping-method` | Установить параметры отгрузки поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/v3/supplies/{supplyId}/deliver` | Передать поставку в доставку | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/supplies/{supplyId}/barcode` | Получить QR-код поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/supplies/{supplyId}/trbx` | Получить список грузомест поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/supplies/{supplyId}/trbx` | Добавить грузоместа к поставке | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| DELETE | `/api/v3/supplies/{supplyId}/trbx` | Удалить грузоместа из поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/v3/supplies/{supplyId}/trbx/stickers` | Получить стикеры грузомест поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/dictionaries/countries/oksm` | Получить список стран ОКСМ | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PUT | `/api/marketplace/v3/fbs/supplies/{supplyId}/spot` | Добавить данные СПОТ в поставку | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/marketplace/v3/fbs/supplies/spot/list` | Получить данные СПОТ для списка поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/supplies/{supplyId}/stickers/spot` | Получить QR-код СПОТ | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/settings/autoreturns` | Получить настройки автовозврата продавца | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/marketplace/v3/fbs/settings/autoreturns` | Обновить настройки автовозврата продавца | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| POST | `/api/marketplace/v3/fbs/settings/autoreturns/items` | Получить настройки автовозврата товаров | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| PATCH | `/api/marketplace/v3/fbs/settings/autoreturns/items` | Обновить настройки автовозврата товаров | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/marketplace/v3/fbs/settings/autoreturns/subcategories/restricted` | Получить предметы, которые не хранятся на складах WB | [описание](https://dev.wildberries.ru/swagger/orders-fbs) |
| GET | `/api/v3/dbw/orders/new` | Получить список новых сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| GET | `/api/v3/dbw/orders` | Получить информацию о завершенных сборочных заданиях | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/v3/dbw/orders/delivery-date` | Получить дату и время доставки | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/marketplace/v3/dbw/orders/client` | Информация о покупателе | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/v3/dbw/orders/status` | Получить статусы сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| PATCH | `/api/v3/dbw/orders/{orderId}/confirm` | Перевести на сборку | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/v3/dbw/orders/stickers` | Получить стикеры сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/marketplace/v3/dbw/orders/status/deliver` | Перевести сборочные задания в доставку | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/v3/dbw/orders/courier` | Информация о курьере | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| PATCH | `/api/v3/dbw/orders/{orderId}/cancel` | Отменить сборочное задание | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/marketplace/v3/dbw/orders/meta/details` | Получить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/marketplace/v3/dbw/orders/meta/delete` | Удалить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| POST | `/api/marketplace/v3/dbw/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| PUT | `/api/v3/dbw/orders/{orderId}/meta/uin` | Закрепить УИН за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| PUT | `/api/v3/dbw/orders/{orderId}/meta/imei` | Закрепить IMEI за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| PUT | `/api/v3/dbw/orders/{orderId}/meta/gtin` | Закрепить GTIN за сборочным заданием | [описание](https://dev.wildberries.ru/swagger/orders-dbw) |
| GET | `/api/v3/dbs/orders/new` | Получить список новых сборочных заданий | [описание](https://dev.wildberries.ru/swagger/dbs) |
| GET | `/api/v3/dbs/orders` | Получить информацию о завершенных сборочных заданиях | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/final-price` | Получить цены продавца и суммы к оплате | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/v3/dbs/groups/info` | Получить информацию о платной доставке | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/v3/dbs/orders/client` | Информация о покупателе | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/b2b/info` | Информация о покупателе B2B | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/v3/dbs/orders/delivery-date` | Получить дату и время доставки | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/info` | Получить статусы сборочных заданий | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/cancel` | Отменить сборочные задания | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/confirm` | Перевести сборочные задания на сборку | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/stickers` | Получить стикеры для сборочных заданий с доставкой в ПВЗ | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/deliver` | Перевести сборочные задания в доставку | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/receive` | Сообщить о получении заказов | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/status/reject` | Сообщить об отказе от заказов | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/details` | Получить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/delete` | Удалить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/uin` | Закрепить УИН за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/imei` | Закрепить IMEI за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/dbs) |
| POST | `/api/marketplace/v3/dbs/orders/meta/customs-declaration` | Закрепить номера ДТ за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/dbs) |
| GET | `/api/v3/click-collect/orders/new` | Получить список новых сборочных заданий | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| GET | `/api/v3/click-collect/orders` | Получить информацию о завершённых сборочных заданиях | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/final-price` | Получить цены продавца и суммы к оплате | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/confirm` | Перевести сборочные задания на сборку | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/prepare` | Сообщить, что сборочные задания готовы к выдаче | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/v3/click-collect/orders/client` | Информация о покупателе | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/v3/click-collect/orders/client/identity` | Проверить, что заказ принадлежит покупателю | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/receive` | Сообщить, что заказы приняты покупателями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/reject` | Сообщить об отказе от заказов | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/info` | Получить статусы сборочных заданий | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/status/cancel` | Отменить сборочные задания | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/details` | Получить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/delete` | Удалить идентификаторы маркировки сборочных заданий | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/uin` | Закрепить УИН за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/imei` | Закрепить IMEI за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/marketplace/v3/click-collect/orders/meta/customs-declaration` | Закрепить номера ДТ за сборочными заданиями | [описание](https://dev.wildberries.ru/swagger/in-store-pickup) |
| POST | `/api/v1/acceptance/options` | Опции приёмки | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/v1/warehouses` | Список складов | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/v1/transit-tariffs` | Транзитные направления | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| POST | `/api/v1/supplies` | Список поставок | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/v1/supplies/{ID}` | Детали поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/v1/supplies/{ID}/goods` | Товары поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/v1/supplies/{ID}/package` | Упаковка поставки | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/supplies/v1/drafts` | Список черновиков | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| POST | `/api/supplies/v1/drafts` | Создать черновик | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| DELETE | `/api/supplies/v1/drafts/{draftId}` | Удалить черновик | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/supplies/v1/drafts/{draftId}/items` | Список товаров в черновике | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| POST | `/api/supplies/v1/drafts/{draftId}/items` | Добавить товары в черновик | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| DELETE | `/api/supplies/v1/drafts/{draftId}/items` | Удалить товары из черновика | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/api/supplies/v1/discrepancies/{supplyId}` | Расхождения в поставке | [описание](https://dev.wildberries.ru/swagger/orders-fbw) |
| GET | `/adv/v1/promotion/count` | Списки кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v3/adverts` | Информация о кампаниях | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v2/adverts` | Информация о кампаниях | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/api/advert/v1/bids/min` | Минимальные ставки для карточек товаров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v2/seacat/save-ad` | Создать кампанию | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/supplier/subjects` | Предметы для кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v2/supplier/nms` | Карточки товаров для кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v0/delete` | Удаление кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/rename` | Переименование кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v0/start` | Запуск кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v0/pause` | Пауза кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v0/stop` | Завершение кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| PUT | `/adv/v0/auction/placements` | Изменение мест размещения в кампаниях с ручной ставкой | [описание](https://dev.wildberries.ru/swagger/promotion) |
| PATCH | `/api/advert/v1/bids` | Изменение ставок в кампаниях | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/balance` | Баланс | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/api/advert/v2/budget` | Остатки бюджетов кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/budget` | Бюджет кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v1/budget/deposit` | Пополнение бюджета кампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/upd` | Получение истории затрат | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/payments` | Получение истории пополнений счёта | [описание](https://dev.wildberries.ru/swagger/promotion) |
| PATCH | `/adv/v0/auction/nms` | Изменение списка карточек товаров в кампаниях | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v0/bids/recommendations` | Рекомендуемые ставки для карточек товаров и поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/stats` | Статистика поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/get-bids` | Список ставок поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v1/config` | Конфигурационные значения продвижения | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/api/advert/v1/normquery/bids` | Установить ставки для поисковых кластеров в валюте профиля продавца | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/bids` | Установить ставки для поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| DELETE | `/adv/v0/normquery/bids` | Удалить ставки поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/get-minus` | Список минус-фраз кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/set-minus` | Установка и удаление минус-фраз | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/count` | Количество медиакампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/adverts` | Список медиакампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v1/advert` | Информация о медиакампании | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/adv/v3/fullstats` | Статистика кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v1/stats` | Статистика медиакампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/v1/calendar/promotions` | Список акций | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/v1/calendar/promotions/details` | Детальная информация об акциях | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/v1/calendar/promotions/nomenclatures` | Список товаров для участия в акции | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/api/v1/calendar/promotions/upload` | Добавить товар в акцию | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v0/normquery/list` | Списки активных и неактивных поисковых кластеров | [описание](https://dev.wildberries.ru/swagger/promotion) |
| POST | `/adv/v1/normquery/stats` | Статистика по поисковым кластерам с детализацией по дням | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v0/daily-limits` | Получить настройки дневных лимитов кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| PUT | `/api/advert/v0/daily-limits` | Настройка дневных лимитов кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v4/fullstats` | Плоская статистика кампаний | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/advert/v0/positions` | Позиции карточек товаров в поисковой выдаче | [описание](https://dev.wildberries.ru/swagger/promotion) |
| GET | `/api/v1/new-feedbacks-questions` | Непросмотренные отзывы и вопросы | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/questions/count-unanswered` | Неотвеченные вопросы | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/questions/count` | Количество вопросов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/questions` | Список вопросов | [описание](https://dev.wildberries.ru/swagger/communications) |
| PATCH | `/api/v1/questions` | Работа с вопросами | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/question` | Получить вопрос по ID | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/feedbacks/count-unanswered` | Необработанные отзывы | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/feedbacks/count` | Количество отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/feedbacks` | Список отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| POST | `/api/v1/feedbacks/answer` | Ответить на отзыв | [описание](https://dev.wildberries.ru/swagger/communications) |
| PATCH | `/api/v1/feedbacks/answer` | Отредактировать ответ на отзыв | [описание](https://dev.wildberries.ru/swagger/communications) |
| POST | `/api/v1/feedbacks/order/return` | Возврат товара по ID отзыва | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/feedback` | Получить отзыв по ID | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/feedbacks/archive` | Список архивных отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/feedbacks/v1/pins` | Список закреплённых и откреплённых отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| POST | `/api/feedbacks/v1/pins` | Закрепить отзывы | [описание](https://dev.wildberries.ru/swagger/communications) |
| DELETE | `/api/feedbacks/v1/pins` | Открепить отзывы | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/feedbacks/v1/pins/count` | Количество закреплённых и откреплённых отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/feedbacks/v1/pins/limits` | Лимиты закреплённых отзывов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/seller/chats` | Список чатов | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/seller/events` | События чатов | [описание](https://dev.wildberries.ru/swagger/communications) |
| POST | `/api/v1/seller/message` | Отправить сообщение | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/seller/download/{id}` | Получить файл из сообщения | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/claims` | Заявки покупателей на возврат | [описание](https://dev.wildberries.ru/swagger/communications) |
| PATCH | `/api/v1/claim` | Ответ на заявку покупателя | [описание](https://dev.wildberries.ru/swagger/communications) |
| GET | `/api/v1/tariffs/commission` | Комиссия по категориям товаров | [описание](https://dev.wildberries.ru/swagger/rates) |
| GET | `/api/tariffs/v1/acceptance/coefficients` | Тарифы на поставку | [описание](https://dev.wildberries.ru/swagger/rates) |
| GET | `/api/v1/tariffs/box` | Тарифы для коробов | [описание](https://dev.wildberries.ru/swagger/rates) |
| GET | `/api/v1/tariffs/pallet` | Тарифы для монопаллет | [описание](https://dev.wildberries.ru/swagger/rates) |
| GET | `/api/v1/tariffs/return` | Тарифы на возврат | [описание](https://dev.wildberries.ru/swagger/rates) |
| POST | `/api/analytics/v3/sales-funnel/products` | Статистика карточек товаров за период | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v3/sales-funnel/products/history` | Статистика карточек товаров по дням | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v3/sales-funnel/grouped/history` | Статистика групп карточек товаров по дням | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/nm-report/downloads` | Создать отчёт | [описание](https://dev.wildberries.ru/swagger/analytics) |
| GET | `/api/v2/nm-report/downloads` | Получить список отчётов | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/nm-report/downloads/retry` | Сгенерировать отчёт повторно | [описание](https://dev.wildberries.ru/swagger/analytics) |
| GET | `/api/v2/nm-report/downloads/file/{downloadId}` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/search-report/report` | Основная страница | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/search-report/table/groups` | Пагинация по группам | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/search-report/table/details` | Пагинация по товарам в группе | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/search-report/product/search-texts` | Поисковые запросы по товару | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/search-report/product/orders` | Заказы и позиции по поисковым запросам товара | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v1/stocks-report/wb-warehouses` | Остатки на складах WB | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v1/stocks-report/seller-warehouses` | Остатки на складах продавца | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/stocks-report/products/groups` | Данные по группам | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/stocks-report/products/products` | Данные по товарам | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/stocks-report/products/sizes` | Данные по размерам | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/v2/stocks-report/offices` | Данные по складам | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v2/item-rating` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/analytics) |
| POST | `/api/analytics/v1/order-feed` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/analytics) |
| GET | `/api/v1/supplier/orders` | Заказы | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/supplier/sales` | Продажи | [описание](https://dev.wildberries.ru/swagger/reports) |
| POST | `/api/v1/analytics/excise-report` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/warehouse_remains` | Создать отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/warehouse_remains/tasks/{task_id}/status` | Проверить статус | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/warehouse_remains/tasks/{task_id}/download` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/analytics/v1/measurement-penalties` | Удержания за занижение габаритов упаковки | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/analytics/v1/warehouse-measurements` | Замеры склада | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/analytics/v1/deductions` | Подмены и неверные вложения | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/antifraud-details` | Самовыкупы | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/goods-labeling` | Маркировка товара | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/acceptance_report` | Создать отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/acceptance_report/tasks/{task_id}/status` | Проверить статус | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/acceptance_report/tasks/{task_id}/download` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/paid_storage` | Создать отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/paid_storage/tasks/{task_id}/status` | Проверить статус | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/paid_storage/tasks/{task_id}/download` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/brand-share/brands` | Бренды продавца | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/brand-share/parent-subjects` | Родительские категории бренда | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/brand-share` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/analytics/banned-products/blocked` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/analytics/v1/item-returns` | Получить отчёт | [описание](https://dev.wildberries.ru/swagger/reports) |
| GET | `/api/v1/account/balance` | Получить баланс продавца | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/sales-reports/list` | Список отчётов реализации | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/sales-reports/detailed/{reportId}` | Детализации к отчётам реализации по ID отчётов | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/sales-reports/detailed` | Детализации к отчётам реализации за период | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/acquiring/list` | Список отчётов об издержках на приём платежей | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/acquiring/detailed/{reportId}` | Детализации к отчётам об издержках на приём платежей по ID отчётов | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/finance/v1/acquiring/detailed` | Детализации к отчётам об издержках на приём платежей за период | [описание](https://dev.wildberries.ru/swagger/finances) |
| GET | `/api/v1/documents/categories` | Категории документов | [описание](https://dev.wildberries.ru/swagger/finances) |
| GET | `/api/v1/documents/list` | Список документов | [описание](https://dev.wildberries.ru/swagger/finances) |
| GET | `/api/v1/documents/download` | Получить документ | [описание](https://dev.wildberries.ru/swagger/finances) |
| POST | `/api/v1/documents/download/all` | Получить документы | [описание](https://dev.wildberries.ru/swagger/finances) |

## OZON

Операций в документации: 497; уникальных пар метод/путь: 497.

| Метод | Путь | Название | Источник |
|---|---|---|---|
| POST | `/v1/roles` | Получить список ролей и методов по API-ключу | [описание](https://docs.ozon.ru/api/seller/#operation/AccessAPI_RolesByToken) |
| POST | `/v1/seller/info` | Информация о кабинете продавца | [описание](https://docs.ozon.ru/api/seller/#operation/SellerAPI_SellerInfo) |
| POST | `/v1/seller/ozon-logistics/info` | Информация о подключении Ozon Доставки | [описание](https://docs.ozon.ru/api/seller/#operation/SellerAPI_SellerOzonLogisticsInfo) |
| POST | `/v1/description-category/tree` | Дерево категорий и типов товаров | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree) |
| POST | `/v1/description-category/attribute` | Список характеристик категории | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes) |
| POST | `/v1/description-category/attribute/values` | Справочник значений характеристики | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributeValues) |
| POST | `/v1/description-category/attribute/values/search` | Поиск по справочным значениям характеристики | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_SearchAttributeValues) |
| POST | `/v1/product/placement-zone/info` | Получить зоны размещения товаров по SKU перед поставкой | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductPlacementZoneInfo) |
| POST | `/v3/product/import` | Создать или обновить товар | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsV3) |
| POST | `/v1/product/import/info` | Узнать статус добавления или обновления товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetImportProductsInfo) |
| POST | `/v1/product/import-by-sku` | Создать товар по SKU | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsBySKU) |
| POST | `/v1/product/attributes/update` | Обновить характеристики товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateAttributes) |
| POST | `/v2/product/pictures/import` | Загрузить или обновить изображения товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductImportPicturesV2) |
| POST | `/v1/product/pictures/import` | Загрузить или обновить изображения товара Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductImportPictures) |
| POST | `/v3/product/list` | Список товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductList) |
| POST | `/v1/product/rating-by-sku` | Получить контент-рейтинг товаров по SKU | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductRatingBySku) |
| POST | `/v3/product/info/list` | Получить информацию о товарах по идентификаторам | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoList) |
| POST | `/v4/product/info/attributes` | Получить описание характеристик товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductAttributesV4) |
| POST | `/v1/product/info/description` | Получить описание товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoDescription) |
| POST | `/v4/product/info/limit` | Лимиты на ассортимент, создание и обновление товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetUploadQuota) |
| POST | `/v1/product/update/offer-id` | Изменить артикулы товаров из системы продавца | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateOfferID) |
| POST | `/v1/product/archive` | Перенести товар в архив | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductArchive) |
| POST | `/v1/product/unarchive` | Вернуть товар из архива | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUnarchive) |
| POST | `/v2/products/delete` | Удалить товар без SKU из архива | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_DeleteProducts) |
| POST | `/v1/product/info/subscription` | Количество подписавшихся на товар пользователей | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoSubscription) |
| POST | `/v1/product/related-sku/get` | Получить связанные SKU | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductGetRelatedSKU) |
| POST | `/v2/product/pictures/info` | Получить изображения товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductInfoPicturesV2) |
| POST | `/v1/product/info/wrong-volume` | Список товаров с некорректными ОВХ | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductInfoWrongVolume) |
| POST | `/v1/barcode/add` | Привязать штрихкод к товару | [описание](https://docs.ozon.ru/api/seller/#operation/add-barcode) |
| POST | `/v1/barcode/delete` | Отвязать штрихкод от товара | [описание](https://docs.ozon.ru/api/seller/#operation/BarcodeDelete) |
| POST | `/v1/barcode/generate` | Создать штрихкод для товара | [описание](https://docs.ozon.ru/api/seller/#operation/generate-barcode) |
| POST | `/v2/products/stocks` | Обновить количество товаров на складах | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductsStocksV2) |
| POST | `/v4/product/info/stocks` | Информация о количестве товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocks) |
| POST | `/v1/product/info/stocks-by-warehouse/fbo` | Получить информацию об остатках на складах FBO | [описание](https://docs.ozon.ru/api/seller/#operation/GetProductInfoStocksByWarehouseFbo) |
| POST | `/v1/product/info/warehouse/stocks` | Получить информацию по остаткам на складе FBS и rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/ProductInfoWarehouseStocks) |
| POST | `/v2/product/info/stocks-by-warehouse/fbs` | Получить информацию об остатках на складах продавца | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocksByWarehouseFbsV2) |
| POST | `/v1/product/info/stocks-by-warehouse/fbs` | Информация об остатках на складах продавца (FBS и rFBS) | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbs) |
| POST | `/v1/product/import/prices` | Обновить цену | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsPrices) |
| POST | `/v1/product/action/timer/update` | Обновление таймера актуальности минимальной цены | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ActionTimerUpdate) |
| POST | `/v1/product/action/timer/status` | Получить статус установленного таймера | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ActionTimerStatus) |
| POST | `/v5/product/info/prices` | Получить информацию о цене товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoPrices) |
| POST | `/v1/product/info/discounted` | Узнать информацию об уценке и основном товаре по SKU уценённого товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoDiscounted) |
| POST | `/v1/product/update/discount` | Установить скидку на уценённый товар | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateDiscount) |
| GET | `/v1/actions` | Список акций | [описание](https://docs.ozon.ru/api/seller/#operation/Promos) |
| POST | `/v2/actions/candidates` | Получить список товаров, которые могут участвовать в акции | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsCandidates) |
| POST | `/v1/actions/candidates` | Список доступных для акции товаров Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PromosCandidates) |
| POST | `/v2/actions/products` | Получить список товаров, которые участвуют в акции | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsProducts) |
| POST | `/v1/actions/products` | Список участвующих в акции товаров Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PromosProducts) |
| POST | `/v1/actions/products/activate` | Добавить товар в акцию Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PromosProductsActivate) |
| POST | `/v1/actions/products/update` | Добавить или обновить товар в акции | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsProductsUpdate) |
| POST | `/v2/actions/products/deactivate` | Удалить товары из акции «Промокоды» | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsProductsDeactivate) |
| POST | `/v1/actions/products/deactivate` | Удалить товары из акции Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PromosProductsDeactivate) |
| POST | `/v1/actions/discounts-task/list` | Список заявок на скидку | [описание](https://docs.ozon.ru/api/seller/#operation/promos_task_list) |
| POST | `/v1/actions/discounts-task/approve` | Согласовать заявку на скидку | [описание](https://docs.ozon.ru/api/seller/#operation/promos_task_approve) |
| POST | `/v1/actions/discounts-task/decline` | Отклонить заявку на скидку | [описание](https://docs.ozon.ru/api/seller/#operation/promos_task_decline) |
| POST | `/v2/actions/auto-add/products/list` | Получить список товаров из автодобавления в акцию | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsListV2) |
| POST | `/v2/actions/auto-add/products/candidates` | Получить список доступных товаров для автодобавления в акцию | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsCandidatesV2) |
| POST | `/v2/actions/auto-add/products/delete` | Удалить товары из автодобавления в акцию | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsDeleteV2) |
| POST | `/v2/actions/auto-add/products/update` | Добавить или обновить товары в автодобавлении в акцию | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsUpdateV2) |
| POST | `/v1/pricing-strategy/competitors/list` | Список конкурентов | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_competitors) |
| POST | `/v1/pricing-strategy/list` | Список стратегий | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_list) |
| POST | `/v1/pricing-strategy/create` | Создать стратегию | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_create) |
| POST | `/v1/pricing-strategy/info` | Информация о стратегии | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_info) |
| POST | `/v1/pricing-strategy/update` | Обновить стратегию | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_update) |
| POST | `/v1/pricing-strategy/products/add` | Добавить товары в стратегию | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_items-add) |
| POST | `/v1/pricing-strategy/strategy-ids-by-product-ids` | Список идентификаторов стратегий | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_ids) |
| POST | `/v1/pricing-strategy/products/list` | Список товаров в стратегии | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_items-list) |
| POST | `/v1/pricing-strategy/product/info` | Цена товара у конкурента | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_items-info) |
| POST | `/v1/pricing-strategy/products/delete` | Удалить товары из стратегии | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_items-delete) |
| POST | `/v1/pricing-strategy/status` | Изменить статус стратегии | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_status) |
| POST | `/v1/pricing-strategy/delete` | Удалить стратегию | [описание](https://docs.ozon.ru/api/seller/#operation/pricing_delete) |
| POST | `/v1/brand/company-certification/list` | Список сертифицируемых брендов | [описание](https://docs.ozon.ru/api/seller/#operation/BrandAPI_BrandCompanyCertificationList) |
| GET | `/v1/product/certificate/accordance-types` | Список типов соответствия требованиям (версия 1) | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateAccordanceTypes) |
| GET | `/v2/product/certificate/accordance-types/list` | Список типов соответствия требованиям (версия 2) | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateAccordanceTypes) |
| GET | `/v1/product/certificate/types` | Справочник типов документов | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateTypes) |
| POST | `/v2/product/certification/list` | Список сертифицируемых категорий | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificationList) |
| POST | `/v1/product/certification/list` | Список сертифицируемых категорий | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_V1ProductCertificationList) |
| POST | `/v2/product/certification/options` | Получить параметры для создания сертификата качества | [описание](https://docs.ozon.ru/api/seller/#operation/ProductCertificateOptions) |
| POST | `/v2/product/certification/params` | Получить обязательные параметры для создания сертификата качества | [описание](https://docs.ozon.ru/api/seller/#operation/ProductCertificateParams) |
| POST | `/v2/product/certificate/create` | Создать сертификат качества | [описание](https://docs.ozon.ru/api/seller/#operation/ProductCertificateCreate) |
| POST | `/v1/product/certificate/create` | Добавить сертификаты для товаров Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateCreate) |
| POST | `/v1/product/certificate/bind` | Привязать сертификат к товару | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateBind) |
| POST | `/v1/product/certificate/delete` | Удалить сертификат | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateDelete) |
| POST | `/v1/product/certificate/info` | Информация о сертификате | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateInfo) |
| POST | `/v1/product/certificate/list` | Список сертификатов | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateList) |
| POST | `/v1/product/certificate/product_status/list` | Список возможных статусов товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductStatusList) |
| POST | `/v2/product/certificate/products/list` | Получить список товаров, которые привязаны к сертификату | [описание](https://docs.ozon.ru/api/seller/#operation/ProductCertificateProductsListV2) |
| POST | `/v1/product/certificate/products/list` | Список товаров, привязанных к сертификату Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateProductsList) |
| POST | `/v1/product/certificate/unbind` | Отвязать товар от сертификата | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateUnbind) |
| POST | `/v1/product/certificate/rejection_reasons/list` | Возможные причины отклонения сертификата | [описание](https://docs.ozon.ru/api/seller/#operation/RejectionReasonsList) |
| POST | `/v1/product/certificate/status/list` | Возможные статусы сертификатов | [описание](https://docs.ozon.ru/api/seller/#operation/CertificateStatusList) |
| POST | `/v2/warehouse/list` | Список складов | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseListV2) |
| POST | `/v1/warehouse/list` | Список складов | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_WarehouseList) |
| POST | `/v2/delivery-method/list` | Список методов доставки realFBS-склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodListV2) |
| POST | `/v1/delivery-method/list` | Список методов доставки склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodList) |
| POST | `/v1/delivery-method/return/settings/get` | Получить информацию по возвратным настройкам rFBS и rFBS Express | [описание](https://docs.ozon.ru/api/seller/#operation/GetDeliveryMethodReturnSettingsV1) |
| POST | `/v1/warehouse/operation/status` | Получить статус операции | [описание](https://docs.ozon.ru/api/seller/#operation/GetWarehouseFBSOperationStatus) |
| POST | `/v1/warehouse/archive` | Перенести склад в архив | [описание](https://docs.ozon.ru/api/seller/#operation/ArchiveWarehouseFBS) |
| POST | `/v1/warehouse/unarchive` | Перенести склад из архива | [описание](https://docs.ozon.ru/api/seller/#operation/UnarchiveWarehouseFBS) |
| POST | `/v1/warehouse/invalid-products/get` | Получить список товаров с ограничениями по доставке | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseInvalidProductsGet) |
| POST | `/v1/warehouse/warehouses-with-invalid-products` | Получить список складов с ограниченными для доставки товарами | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseWithInvalidProducts) |
| POST | `/v1/warehouse/fbs/create/drop-off/list` | Получить список drop-off пунктов для создания склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse) |
| POST | `/v1/warehouse/fbs/update/drop-off/list` | Получить список drop-off пунктов для изменения информации склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_ListDropOffPointsForUpdateFBSWarehouse) |
| POST | `/v1/warehouse/fbs/create/drop-off/timeslot/list` | Получить список таймслотов для создания склада с отгрузкой drop-off | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsCreateDropOffTimeslotList) |
| POST | `/v1/warehouse/fbs/update/drop-off/timeslot/list` | Получить список таймслотов для обновления склада с отгрузкой drop-off | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsUpdateDropOffTimeslotList) |
| POST | `/v1/warehouse/fbs/create/pick-up/timeslot/list` | Получить список таймслотов для создания склада с отгрузкой pick-up | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsCreatePickUpTimeslotList) |
| POST | `/v1/warehouse/fbs/update/pick-up/timeslot/list` | Получить список таймслотов для обновления склада с отгрузкой pick-up | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsUpdatePickUpTimeslotList) |
| POST | `/v1/warehouse/fbs/create` | Создать склад | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_CreateWarehouseFBS) |
| POST | `/v1/warehouse/fbs/update` | Обновить склад | [описание](https://docs.ozon.ru/api/seller/#operation/UpdateWarehouseFBS) |
| POST | `/v1/warehouse/fbs/first-mile/update` | Обновить первую милю | [описание](https://docs.ozon.ru/api/seller/#operation/UpdateWarehouseFBSFirstMile) |
| POST | `/v1/warehouse/fbs/create/return-point/list` | Получить список пунктов возврата для создания склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFBSCreateReturnPointList) |
| POST | `/v1/warehouse/fbs/update/return-point/list` | Получить список пунктов возврата для обновления склада | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFBSUpdateReturnPointList) |
| POST | `/v1/warehouse/fbs/return-mile/info` | Получить информацию о возвратной миле | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFBSReturnMileInfo) |
| POST | `/v1/warehouse/fbs/return-mile/check` | Проверить необходимость установки возвратной мили на склад | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsReturnMileCheck) |
| POST | `/v1/warehouse/fbs/pickup/courier/create` | Создать вызов курьера на забор отгрузки pick-up | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpCourierCreate) |
| POST | `/v1/warehouse/fbs/pickup/courier/cancel` | Отменить вызов курьера на забор отгрузки pick-up | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpCourierCancel) |
| POST | `/v1/warehouse/fbs/pickup/history/list` | Получить историю отгрузок курьерам | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpHistoryList) |
| POST | `/v1/warehouse/fbs/pickup/planning/list` | Получить список складов для планирования отгрузок курьеру | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpPlanningList) |
| POST | `/v1/warehouse/erfbs/aggregator/create` | Создать склад с методом доставки «Партнёры Ozon» | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSAggregatorCreate) |
| POST | `/v1/warehouse/erfbs/update` | Обновить склад | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSUpdate) |
| POST | `/v1/warehouse/erfbs/aggregator/delivery-method/update` | Обновить метод доставки «Партнёры Ozon» | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSAggregatorDeliveryMethodUpdate) |
| POST | `/v1/warehouse/erfbs/non-integrated/create` | Создать склад с методом доставки «Вы или сторонняя служба» | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSNonIntegratedCreate) |
| POST | `/v1/warehouse/erfbs/non-integrated/delivery-method/update` | Обновить метод доставки «Вы или сторонняя служба» | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSNonIntegratedDeliveryMethodUpdate) |
| POST | `/v1/warehouse/rfbs/pause` | Поставить rFBS-склад на паузу | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseRfbsPause) |
| POST | `/v1/warehouse/rfbs/unpause` | Снять rFBS-склад с паузы | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseRfbsUnpause) |
| POST | `/v4/posting/fbs/unfulfilled/list` | Получить список необработанных отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsUnfulfilledList) |
| POST | `/v3/posting/fbs/unfulfilled/list` | Список необработанных отправлений Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingUnfulfilledList) |
| POST | `/v4/posting/fbs/list` | Получить список отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsList) |
| POST | `/v3/posting/fbs/list` | Список отправлений Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingListV3) |
| POST | `/v3/posting/fbs/get` | Получить информацию об отправлении по идентификатору | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingV3) |
| POST | `/v2/posting/fbs/get-by-barcode` | Получить информацию об отправлении по штрихкоду | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingByBarcode) |
| POST | `/v3/posting/multiboxqty/set` | Указать количество коробок для многокоробочных отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingMultiBoxQtySetV3) |
| POST | `/v2/posting/fbs/product/country/list` | Список доступных стран-изготовителей | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_ListCountryProductFbsPostingV2) |
| POST | `/v2/posting/fbs/product/country/set` | Добавить информацию о стране-изготовителе товара | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_SetCountryProductFbsPostingV2) |
| POST | `/v1/posting/fbs/restrictions` | Получить ограничения пункта приёма | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetRestrictions) |
| POST | `/v2/posting/fbs/package-label` | Напечатать этикетку Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSPackageLabel) |
| POST | `/v3/posting/fbs/package-label/create` | Создать задание на формирование этикеток | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsPackageLabelCreate) |
| POST | `/v2/posting/fbs/package-label/create` | Создать задание на формирование этикеток Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_CreateLabelBatchV2) |
| POST | `/v1/posting/fbs/package-label/create` | Создать задание на выгрузку этикеток Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_CreateLabelBatch) |
| POST | `/v2/posting/fbs/package-label/get` | Получить файл с этикетками | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsPackageLabelGet) |
| POST | `/v1/posting/fbs/package-label/get` | Получить файл с этикетками Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetLabelBatch) |
| POST | `/v1/posting/fbs/cancel-reason` | Причины отмены отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetPostingFbsCancelReasonV1) |
| POST | `/v2/posting/fbs/cancel-reason/list` | Причины отмены отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetPostingFbsCancelReasonList) |
| POST | `/v2/posting/fbs/product/cancel` | Отменить отправку некоторых товаров в отправлении | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPostingProduct) |
| POST | `/v2/posting/fbs/cancel` | Отменить отправление | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPosting) |
| POST | `/v2/posting/fbs/arbitration` | Открыть спор по отправлению | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_MoveFbsPostingToArbitration) |
| POST | `/v2/posting/fbs/awaiting-delivery` | Передать отправление к отгрузке | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_MoveFbsPostingToAwaitingDelivery) |
| POST | `/v1/posting/fbs/pick-up-code/verify` | Проверить код курьера | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSPickupCodeVerify) |
| POST | `/v1/posting/global/etgb` | Таможенные декларации ETGB | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb) |
| POST | `/v1/posting/unpaid-legal/product/list` | Список неоплаченных товаров, заказанных юридическими лицами | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_UnpaidLegalProductList) |
| POST | `/v1/polygon/create` | Создайте полигон доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonAPI_CreatePolygon) |
| POST | `/v2/polygon/bind` | Связать метод доставки с полигоном | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonBind) |
| POST | `/v1/polygon/bind` | Свяжите метод доставки с полигоном доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonAPI_BindPolygon) |
| POST | `/v1/polygon/delete` | Удалить полигон из области доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonDelete) |
| POST | `/v1/polygon/list` | Получить список установленных полигонов на метод доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonList) |
| POST | `/v1/polygon/time/coordinates/update` | Обновить координаты полигона доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonTimeCoordinatesUpdate) |
| POST | `/v1/polygon/time/set` | Установить новое время доставки в полигоне | [описание](https://docs.ozon.ru/api/seller/#operation/PolygonTimeSet) |
| POST | `/v3/posting/fbo/list` | Получить список отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFboList) |
| POST | `/v2/posting/fbo/list` | Список отправлений Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFboPostingList) |
| POST | `/v2/posting/fbo/get` | Информация об отправлении | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFboPosting) |
| POST | `/v1/posting/fbo/cancel-reason/list` | Причины отмены отправлений по схеме FBO | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetPostingFboCancelReasonList) |
| POST | `/v1/supply-order/status/counter` | Количество заявок по статусам | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderStatusCounter) |
| POST | `/v1/supply-order/bundle` | Состав поставки или заявки на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderBundle) |
| POST | `/v3/supply-order/list` | Список заявок на поставку на склад Ozon | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderList) |
| POST | `/v3/supply-order/get` | Информация о заявке на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderGet) |
| POST | `/v1/supply-order/timeslot/get` | Интервалы поставки | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_GetSupplyOrderTimeslots) |
| POST | `/v2/supply-order/timeslot/list` | Получить список доступных интервалов поставки | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderTimeslotList) |
| POST | `/v1/supply-order/timeslot/update` | Обновить интервал поставки | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_UpdateSupplyOrderTimeslot) |
| POST | `/v1/supply-order/timeslot/status` | Статус интервала поставки | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_GetSupplyOrderTimeslotStatus) |
| POST | `/v1/supply-order/pass/create` | Указать данные о водителе и автомобиле | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderPassCreate) |
| POST | `/v1/supply-order/pass/status` | Статус ввода данных о водителе и автомобиле | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderPassStatus) |
| POST | `/v1/supply-order/details` | Получить подробную информацию о заявке на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderDetails) |
| GET | `/v1/supplier/available_warehouses` | Загруженность складов Ozon | [описание](https://docs.ozon.ru/api/seller/#operation/SupplierAPI_SupplierAvailableWarehouses) |
| POST | `/v2/cluster/list` | Получить информацию о макролокальных кластерах | [описание](https://docs.ozon.ru/api/seller/#operation/DraftClusterList) |
| POST | `/v1/cluster/list` | Информация о кластерах и их складах | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyDraftAPI_DraftClusterList) |
| POST | `/v1/warehouse/fbo/list` | Поиск точек для отгрузки поставки | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyDraftAPI_DraftGetWarehouseFboList) |
| POST | `/v1/draft/crossdock/create` | Создать черновик заявки на поставку кросс-докингом | [описание](https://docs.ozon.ru/api/seller/#operation/DraftCrossdockCreate) |
| POST | `/v1/draft/direct/create` | Создать черновик заявки на прямую поставку | [описание](https://docs.ozon.ru/api/seller/#operation/DraftDirectCreate) |
| POST | `/v1/draft/multi-cluster/create` | Создать черновик заявки на поставку для нескольких кластеров | [описание](https://docs.ozon.ru/api/seller/#operation/DraftMultiClusterCreate) |
| POST | `/v2/draft/create/info` | Получить информацию о черновике заявки на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/DraftCreateInfo) |
| POST | `/v2/draft/timeslot/info` | Получить список доступных таймслотов | [описание](https://docs.ozon.ru/api/seller/#operation/DraftTimeslotInfo) |
| POST | `/v1/cargoes/create` | Установка грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesCreate) |
| POST | `/v2/cargoes/create/info` | Получить информацию по установке грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesCreateInfoV2) |
| POST | `/v2/cargoes/get` | Получить информацию о грузоместах | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesGetV2) |
| POST | `/v1/cargoes/get` | Получить информацию о грузоместах | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesGet) |
| POST | `/v2/cargoes/delete` | Удалить грузоместа и транспортные грузоместа в заявке на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesDeleteV2) |
| POST | `/v1/cargoes/delete` | Удалить грузоместо в заявке на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDelete) |
| POST | `/v2/cargoes/delete/status` | Получить информацию о статусе удаления грузомест и транспортных грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesDeleteStatusV2) |
| POST | `/v1/cargoes/delete/status` | Информация о статусе удаления грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDeleteStatus) |
| POST | `/v1/cargoes/rules/get` | Чек-лист по установке грузомест FBO | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesRulesGet) |
| POST | `/v1/cargoes-label/create` | Сгенерировать этикетки для грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesLabelCreate) |
| POST | `/v1/cargoes-label/get` | Получить идентификатор этикетки для грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesLabelGet) |
| POST | `/v1/supply-order/cancel` | Отменить заявку на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderCancel) |
| POST | `/v1/supply-order/cancel/status` | Получить статус отмены заявки на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderCancelStatus) |
| POST | `/v1/supply-order/content/update` | Редактирование товарного состава | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderContentUpdate) |
| POST | `/v1/supply-order/content/update/status` | Информация о статусе редактирования товарного состава | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderContentUpdateStatus) |
| POST | `/v1/supply-order/content/update/validation` | Проверить новый товарный состав | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderContentUpdateValidation) |
| POST | `/v2/draft/supply/create` | Создать заявку на поставку по черновику | [описание](https://docs.ozon.ru/api/seller/#operation/DraftSupplyCreate) |
| POST | `/v2/draft/supply/create/status` | Получить информацию о создании заявки на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/DraftSupplyCreateStatus) |
| POST | `/v1/warehouse/fbo/seller/list` | Получить список складов продавца | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseFboSellerList) |
| POST | `/v1/cargoes/transport/activate` | Включить или отключить транспортные грузоместа в поставке | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportActivate) |
| POST | `/v1/cargoes/transport/activate/status` | Получить статус включения или отключения транспортных грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportActivateStatus) |
| POST | `/v1/cargoes/transport/create` | Создать транспортное грузоместо | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportCreate) |
| POST | `/v1/cargoes/transport/create/status` | Получить статус создания транспортного грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportCreateStatus) |
| POST | `/v1/cargoes/transport/bind` | Связать или отвязать грузоместа и транспортные грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportBind) |
| POST | `/v1/cargoes/transport/bind/status` | Получить статус связывания или отвязывания грузомест и транспортных грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesTransportBindStatus) |
| POST | `/v1/cargoes/supplies/get` | Получить информацию о грузоместах в поставках | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesSuppliesGet) |
| POST | `/v1/cargoes/label/transport-by-order/create` | Сгенерировать этикетки для транспортных грузомест по идентификатору поставки | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesLabelTransportByOrderCreate) |
| POST | `/v1/cargoes/label/transport-by-order/status` | Получить статус генерации этикеток для транспортных грузомеcт по идентификатору поставки | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesLabelTransportByOrderStatus) |
| POST | `/v1/cargoes/label/transport/create` | Сгенерировать этикетки транспортных грузомест по идентификатору грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesLabelTransportCreate) |
| POST | `/v1/cargoes/label/transport/status` | Получить статус генерации этикеток транспортных грузомест по идентификатору грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CargoesLabelTransportStatus) |
| POST | `/v1/supply-order/act/summary/get` | Получить информацию об акте | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderActSummaryGet) |
| POST | `/v1/supply-order/act/product/get` | Получить информацию о товарах в акте | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderActProductGet) |
| POST | `/v1/supply-order/act/accept` | Согласовать акт | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderActAccept) |
| POST | `/v1/supply-order/act/accept/status` | Получить статус согласования акта | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderActAcceptStatus) |
| POST | `/v1/warehouse/ozon/list` | Получить список складов Ozon | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseOZONList) |
| POST | `/v4/posting/fbs/ship` | Собрать заказ (версия 4) | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_ShipFbsPostingV4) |
| POST | `/v4/posting/fbs/ship/package` | Частичная сборка отправления (версия 4) | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_ShipFbsPostingPackage) |
| POST | `/v6/fbs/posting/product/exemplar/set` | Проверить и сохранить данные экземпляров | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarSetV6) |
| POST | `/v6/fbs/posting/product/exemplar/create-or-get` | Получить данные созданных экземпляров | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarCreateOrGetV6) |
| POST | `/v5/fbs/posting/product/exemplar/status` | Получить статус добавления экземпляров | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarStatusV5) |
| POST | `/v5/fbs/posting/product/exemplar/validate` | Валидация кодов маркировки | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarValidateV5) |
| POST | `/v1/fbs/posting/product/exemplar/update` | Обновить данные экземпляров | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarUpdate) |
| POST | `/v1/carriage/create` | Создание отгрузки | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCreate) |
| POST | `/v1/carriage/approve` | Подтверждение отгрузки | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageApprove) |
| POST | `/v1/carriage/set-postings` | Изменение состава отгрузки | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_SetPostings) |
| POST | `/v1/carriage/cancel` | Удаление отгрузки | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCancel) |
| POST | `/v2/carriage/delivery/list` | Список методов доставки и отгрузок | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryListV2) |
| POST | `/v1/carriage/delivery/list` | Список методов доставки и отгрузок | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryList) |
| POST | `/v2/posting/fbs/act/create` | Подтвердить отгрузку и создать документы | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCreate) |
| POST | `/v1/posting/carriage-available/list` | Список доступных перевозок | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetCarriageAvailableList) |
| POST | `/v1/carriage/get` | Информация о перевозке | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageGet) |
| POST | `/v1/carriage/courier-contact/set` | Добавить или обновить контактные данные продавца для курьера | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageCourierContactSet) |
| POST | `/v1/carriage/courier-contact/get` | Получить контактные данные продавца для курьера | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageCourierContactGet) |
| POST | `/v1/posting/fbs/split` | Разделить заказ на отправления без сборки | [описание](https://docs.ozon.ru/api/seller/#operation/FbsSplit) |
| POST | `/v2/posting/fbs/act/get-postings` | Список отправлений в акте | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_ActPostingList) |
| POST | `/v2/posting/fbs/act/get-container-labels` | Этикетки для грузового места | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActGetContainerLabels) |
| POST | `/v2/posting/fbs/act/get-barcode` | Штрихкод для отгрузки отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetBarcode) |
| POST | `/v2/posting/fbs/act/get-barcode/text` | Значение штрихкода для отгрузки отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetBarcodeText) |
| POST | `/v2/posting/fbs/digital/act/check-status` | Статус формирования накладной Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSDigitalActCheckStatus) |
| POST | `/v2/posting/fbs/act/get-pdf` | Получить PDF c документами | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetAct) |
| POST | `/v1/carriage/act-discrepancy/pdf` | Получить акт о расхождениях по отгрузке FBS | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageActDiscrepancyPDF) |
| POST | `/v2/posting/fbs/act/list` | Список актов по отгрузкам | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsActList) |
| POST | `/v2/posting/fbs/digital/act/get-pdf` | Получить лист отгрузки по перевозке Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetDigitalAct) |
| POST | `/v2/posting/fbs/act/check-status` | Статус отгрузки и документов | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCheckStatus) |
| POST | `/v1/posting/fbs/traceable/split` | Разделить отправление с прослеживаемыми товарами | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsTraceableSplit) |
| POST | `/v1/posting/fbs/product/traceable/attribute` | Получить список незаполненных атрибутов для прослеживаемых товаров | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbsProductTraceableAttribute) |
| POST | `/v1/carriage/ettn/status` | Получить статус проверки электронной ТТН на прослеживаемой перевозке FBS | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageEttnStatus) |
| POST | `/v1/assembly/carriage/posting/list` | Получить список отправлений в отгрузке | [описание](https://docs.ozon.ru/api/seller/#operation/AssemblyCarriagePostingList) |
| POST | `/v1/assembly/carriage/product/list` | Получить список товаров в отгрузке | [описание](https://docs.ozon.ru/api/seller/#operation/AssemblyCarriageProductList) |
| POST | `/v1/assembly/fbs/posting/list` | Получить список отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/AssemblyFbsPostingList) |
| POST | `/v1/assembly/fbs/product/list` | Получить список товаров в отправлениях | [описание](https://docs.ozon.ru/api/seller/#operation/AssemblyFbsProductList) |
| POST | `/v2/fbs/posting/tracking-number/set` | Добавить трек-номера | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingTrackingNumberSet) |
| POST | `/v2/fbs/posting/delivering` | Изменить статус на «Доставляется» | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingDelivering) |
| POST | `/v2/fbs/posting/last-mile` | Изменить статус на «Последняя миля» | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingLastMile) |
| POST | `/v2/fbs/posting/delivered` | Изменить статус на «Доставлено» | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingDelivered) |
| POST | `/v1/posting/fbs/timeslot/change-restrictions` | Доступные даты для переноса доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingTimeslotChangeRestrictions) |
| POST | `/v1/posting/fbs/timeslot/set` | Перенести дату доставки | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_SetPostingTimeslot) |
| POST | `/v1/posting/cutoff/set` | Уточнить дату отгрузки отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_SetPostingCutoff) |
| POST | `/v1/pass/list` | Список пропусков | [описание](https://docs.ozon.ru/api/seller/#operation/PassList) |
| POST | `/v1/carriage/pass/create` | Создать пропуск | [описание](https://docs.ozon.ru/api/seller/#operation/carriagePassCreate) |
| POST | `/v1/carriage/pass/update` | Обновить пропуск | [описание](https://docs.ozon.ru/api/seller/#operation/carriagePassUpdate) |
| POST | `/v1/carriage/pass/delete` | Удалить пропуск | [описание](https://docs.ozon.ru/api/seller/#operation/carriagePassDelete) |
| POST | `/v1/return/pass/create` | Создать пропуск для возврата | [описание](https://docs.ozon.ru/api/seller/#operation/returnPassCreate) |
| POST | `/v1/return/pass/update` | Обновить пропуск для возврата | [описание](https://docs.ozon.ru/api/seller/#operation/returnPassUpdate) |
| POST | `/v1/return/pass/delete` | Удалить пропуск для возврата | [описание](https://docs.ozon.ru/api/seller/#operation/returnPassDelete) |
| POST | `/v1/returns/list` | Информация о возвратах FBO и FBS | [описание](https://docs.ozon.ru/api/seller/#operation/returnsList) |
| POST | `/v1/returns/settings/utilization/history` | Получить историю изменений автоутилизации | [описание](https://docs.ozon.ru/api/seller/#operation/UtilizationHistory) |
| POST | `/v1/returns/settings/utilization/info` | Получить настройки автоутилизации | [описание](https://docs.ozon.ru/api/seller/#operation/UtilizationInfo) |
| POST | `/v1/returns/settings/utilization/update` | Обновить настройки автоутилизации | [описание](https://docs.ozon.ru/api/seller/#operation/UtilizationUpdate) |
| POST | `/v2/returns/rfbs/list` | Список заявок на возврат | [описание](https://docs.ozon.ru/api/seller/#operation/RFBSReturnsAPI_ReturnsRfbsListV2) |
| POST | `/v2/returns/rfbs/get` | Информация о заявке на возврат | [описание](https://docs.ozon.ru/api/seller/#operation/RFBSReturnsAPI_ReturnsRfbsGetV2) |
| POST | `/v1/returns/rfbs/action/set` | Передать доступные действия для rFBS возвратов | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsActionSet) |
| POST | `/v1/returns/company/fbs/info` | Количество возвратов FBS | [описание](https://docs.ozon.ru/api/seller/#operation/returnsCompanyFBSInfo) |
| POST | `/v1/return/giveout/is-enabled` | Проверить возможность получения возвратных отгрузок по штрихкоду | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutIsEnabled) |
| POST | `/v1/return/giveout/list` | Список возвратных отгрузок | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutList) |
| POST | `/v1/return/giveout/info` | Информация о возвратной отгрузке | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutInfo) |
| POST | `/v1/return/giveout/barcode` | Значение штрихкода для возвратных отгрузок | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutGetBarcode) |
| POST | `/v1/return/giveout/get-pdf` | Штрихкод для получения возвратной отгрузки в формате PDF | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutGetPDF) |
| POST | `/v1/return/giveout/get-png` | Штрихкод для получения возвратной отгрузки в формате PNG | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutGetPNG) |
| POST | `/v1/return/giveout/barcode-reset` | Сгенерировать новый штрихкод | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_GiveoutBarcodeReset) |
| POST | `/v2/conditional-cancellation/list` | Получить список заявок на отмену rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/CancellationAPI_GetConditionalCancellationListV2) |
| POST | `/v2/conditional-cancellation/approve` | Подтвердить заявку на отмену rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/CancellationAPI_ConditionalCancellationApproveV2) |
| POST | `/v2/conditional-cancellation/reject` | Отклонить заявку на отмену rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/CancellationAPI_ConditionalCancellationRejectV2) |
| POST | `/v1/chat/send/file` | Отправить файл | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatSendFile) |
| POST | `/v3/chat/list` | Список чатов | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatListV3) |
| POST | `/v3/chat/history` | История чата | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatHistoryV3) |
| POST | `/v2/invoice/create-or-update` | Создать или изменить счёт-фактуру | [описание](https://docs.ozon.ru/api/seller/#operation/InvoiceAPI_InvoiceCreateOrUpdateV2) |
| POST | `/v1/invoice/file/upload` | Загрузка счёта-фактуры | [описание](https://docs.ozon.ru/api/seller/#operation/invoice_upload) |
| POST | `/v2/invoice/get` | Получить информацию о счёте-фактуре | [описание](https://docs.ozon.ru/api/seller/#operation/invoice_getV2) |
| POST | `/v1/invoice/delete` | Удалить ссылку на счёт-фактуру | [описание](https://docs.ozon.ru/api/seller/#operation/invoice_delete) |
| POST | `/v1/report/info` | Информация об отчёте | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportInfo) |
| POST | `/v1/report/list` | Список отчётов | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportList) |
| POST | `/v1/report/products/create` | Отчёт по товарам | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyProductsReport) |
| POST | `/v2/report/returns/create` | Отчёт о возвратах | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportReturnsCreate) |
| POST | `/v1/report/postings/create` | Отчёт об отправлениях | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyPostingsReport) |
| POST | `/v1/finance/cash-flow-statement/list` | Финансовый отчёт | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceCashFlowStatementList) |
| POST | `/v1/report/discounted/create` | Отчёт об уценённых товарах | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateDiscountedReport) |
| POST | `/v1/report/warehouse/stock` | Отчёт об остатках на FBS-складе | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateStockByWarehouseReport) |
| POST | `/v1/report/placement/by-products/create` | Получить отчёт о стоимости размещения по товарам | [описание](https://docs.ozon.ru/api/seller/#operation/CreatePlacementByProductsReport) |
| POST | `/v1/report/placement/by-supplies/create` | Получить отчёт о стоимости размещения по поставкам | [описание](https://docs.ozon.ru/api/seller/#operation/CreatePlacementBySuppliesReport) |
| POST | `/v1/report/marked-products-sales/create` | Сгенерировать отчёт по продажам товаров с маркировкой | [описание](https://docs.ozon.ru/api/seller/#operation/CreateCompanyMarkedProductsSalesReport) |
| POST | `/v1/report/realization/posting/create` | Получить позаказный отчёт о реализации товаров Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/CreateCompanyFinanceRealizationPostingReport) |
| POST | `/v2/analytics/stock_on_warehouses` | Отчёт по остаткам и товарам | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsGetStockOnWarehousesV2) |
| POST | `/v1/analytics/turnover/stocks` | Оборачиваемость товара | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_StocksTurnover) |
| POST | `/v1/analytics/stocks` | Получить аналитику по остаткам | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsStocks) |
| POST | `/v2/finance/realization` | Отчёт о реализации товаров (версия 2) Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetRealizationReportV2) |
| POST | `/v1/finance/realization/posting` | Позаказный отчёт о реализации товаров Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetRealizationReportV1) |
| POST | `/v3/finance/transaction/list` | Список транзакций | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceTransactionListV3) |
| POST | `/v3/finance/transaction/totals` | Суммы транзакций | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceTransactionTotalV3) |
| POST | `/v1/finance/document-b2b-sales` | Реестр продаж юридическим лицам | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateDocumentB2BSalesReport) |
| POST | `/v1/finance/document-b2b-sales/json` | Реестр продаж юридическим лицам в JSON-формате | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateDocumentB2BSalesJSONReport) |
| POST | `/v1/finance/mutual-settlement` | Отчёт о взаиморасчётах | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateMutualSettlementReport) |
| POST | `/v1/finance/products/buyout` | Отчёт о выкупленных товарах | [описание](https://docs.ozon.ru/api/seller/#operation/GetFinanceProductsBuyout) |
| POST | `/v1/finance/compensation` | Отчёт о компенсациях | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_GetCompensationReport) |
| POST | `/v1/finance/decompensation` | Отчёт о декомпенсациях | [описание](https://docs.ozon.ru/api/seller/#operation/ReportAPI_GetDecompensationReport) |
| POST | `/v1/receipts/get` | Получить чек в формате PDF | [описание](https://docs.ozon.ru/api/seller/#operation/GetReceipt) |
| POST | `/v1/receipts/seller/list` | Получить список чеков продавца | [описание](https://docs.ozon.ru/api/seller/#operation/ReceiptsSellerList) |
| POST | `/v1/receipts/upload` | Загрузить чек | [описание](https://docs.ozon.ru/api/seller/#operation/UploadReceipt) |
| POST | `/v1/rating/summary` | Получить информацию о текущих рейтингах продавца | [описание](https://docs.ozon.ru/api/seller/#operation/RatingAPI_RatingSummaryV1) |
| POST | `/v1/rating/history` | Получить информацию о рейтингах продавца за период | [описание](https://docs.ozon.ru/api/seller/#operation/RatingAPI_RatingHistoryV1) |
| POST | `/v1/rating/index/fbs/info` | Получить индекс ошибок FBS и rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/RatingAPI_GetFBSRatingIndexInfoV1) |
| POST | `/v1/rating/index/fbs/posting/list` | Список отправлений, которые повлияли на индекс ошибок FBS и rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/RatingAPI_ListFBSRatingIndexPostingsV1) |
| POST | `/v1/posting/digital/codes/upload` | Загрузить коды цифровых товаров для отправления | [описание](https://docs.ozon.ru/api/seller/#operation/UploadPostingCodes) |
| POST | `/v1/posting/digital/list` | Получить список отправлений Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ListPostingCodes) |
| POST | `/v1/product/digital/stocks/import` | Обновить количество цифровых товаров | [описание](https://docs.ozon.ru/api/seller/#operation/DigitalProductAPI_StocksImport) |
| POST | `/v1/review/comment/create` | Оставить комментарий на отзыв | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_CommentCreate) |
| POST | `/v2/review/comment/delete` | Удалить комментарий на отзыв | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewCommentDeleteV2) |
| POST | `/v1/review/comment/delete` | Удалить комментарий на отзыв Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_CommentDelete) |
| POST | `/v1/review/comment/list` | Получить список комментариев на отзыв | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_CommentList) |
| POST | `/v2/review/change-status` | Изменить статус отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewChangeStatusV2) |
| POST | `/v1/review/change-status` | Изменить статус отзывов Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_ReviewChangeStatus) |
| POST | `/v2/review/count` | Получить количество отзывов по статусам | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewCountV2) |
| POST | `/v1/review/count` | Количество отзывов по статусам Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_ReviewCount) |
| POST | `/v2/review/info` | Получить информацию по отзыву | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewInfoV2) |
| POST | `/v1/review/info` | Получить информацию об отзыве Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_ReviewInfo) |
| POST | `/v2/review/list` | Получить список отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewListV2) |
| POST | `/v1/review/list` | Получить список отзывов Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewAPI_ReviewList) |
| POST | `/v1/question/answer/create` | Создать ответ на вопрос | [описание](https://docs.ozon.ru/api/seller/#operation/QuestionAnswer_Create) |
| POST | `/v1/question/answer/delete` | Удалить ответ на вопрос | [описание](https://docs.ozon.ru/api/seller/#operation/QuestionAnswer_Delete) |
| POST | `/v1/question/answer/list` | Список ответов на вопрос | [описание](https://docs.ozon.ru/api/seller/#operation/QuestionAnswer_List) |
| POST | `/v1/question/change-status` | Изменить статус вопросов | [описание](https://docs.ozon.ru/api/seller/#operation/Question_ChangeStatus) |
| POST | `/v1/question/count` | Количество вопросов по статусам | [описание](https://docs.ozon.ru/api/seller/#operation/Question_Count) |
| POST | `/v1/question/info` | Информация о вопросе | [описание](https://docs.ozon.ru/api/seller/#operation/Question_Info) |
| POST | `/v1/question/list` | Список вопросов | [описание](https://docs.ozon.ru/api/seller/#operation/Question_List) |
| POST | `/v1/question/top-sku` | Товары с наибольшим количеством вопросов | [описание](https://docs.ozon.ru/api/seller/#operation/Question_TopSku) |
| POST | `/v1/notification/set` | Подключить URL-адрес для уведомлений | [описание](https://docs.ozon.ru/api/seller/#operation/SetNotification) |
| POST | `/v1/notification/update` | Изменить URL-адрес для уведомлений | [описание](https://docs.ozon.ru/api/seller/#operation/UpdateNotification) |
| POST | `/v1/notification/delete` | Удалить URL-адрес для уведомлений | [описание](https://docs.ozon.ru/api/seller/#operation/DeleteNotification) |
| POST | `/v1/notification/check` | Проверить URL-адрес для уведомлений | [описание](https://docs.ozon.ru/api/seller/#operation/CheckNotification) |
| POST | `/v1/notification/enable` | Включить или выключить уведомления на URL-адрес | [описание](https://docs.ozon.ru/api/seller/#operation/EnableNotification) |
| POST | `/v1/notification/list` | Получить информацию по подключённым URL-адресам | [описание](https://docs.ozon.ru/api/seller/#operation/NotificationList) |
| POST | `/v1/notification/push-type/list` | Получить типы пуш-уведомлений | [описание](https://docs.ozon.ru/api/seller/#operation/GetNotificationPushTypeList) |
| POST | `/v1/analytics/manage/stocks` | Управление остатками | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_ManageStocks) |
| POST | `/v1/analytics/decommissioned-goods` | Получить отчёт о списанных товарах | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsDecommissionedGoods) |
| POST | `/v1/analytics/category/comparison` | Получить информацию о сравнении категорий | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsCategoryComparison) |
| POST | `/v1/removal/from-supply/list` | Отчёт по вывозу и утилизации с поставки FBO | [описание](https://docs.ozon.ru/api/seller/#operation/GetSupplyReturnsSummaryReport) |
| POST | `/v1/removal/from-stock/list` | Отчёт по вывозу и утилизации со стока FBO | [описание](https://docs.ozon.ru/api/seller/#operation/GetSupplierReturnsSummaryReport) |
| POST | `/v1/product/stairway-discount/by-quantity/set` | Управлять скидкой от количества | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_SetProductStairwayDiscountByQuantity) |
| POST | `/v1/product/stairway-discount/by-quantity/get` | Получить информацию о скидке от количества | [описание](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductStairwayDiscountByQuantity) |
| POST | `/v1/finance/balance` | Получить отчёт о балансе | [описание](https://docs.ozon.ru/api/seller/#operation/GetFinanceBalanceV1) |
| POST | `/v2/actions/discounts-task/list` | Получить список заявок на скидку | [описание](https://docs.ozon.ru/api/seller/#operation/GetDiscountTaskListV2) |
| POST | `/v1/product/visibility/set` | Настроить видимость товара на витрине Ozon и Ozon Селект | [описание](https://docs.ozon.ru/api/seller/#operation/ProductVisibilitySet) |
| POST | `/v2/posting/digital/list` | Получить список отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingDigitalList) |
| POST | `/v1/finance/accrual/postings` | Получить начисления по отправлениям | [описание](https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualPostings) |
| POST | `/v1/finance/accrual/types` | Получить справочник начислений | [описание](https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualTypes) |
| POST | `/v1/finance/accrual/by-day` | Получить начисления за день | [описание](https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualByDay) |
| POST | `/v1/product/visibility/info` | Получить информацию о видимости товара | [описание](https://docs.ozon.ru/api/seller/#operation/ProductVisibilityInfo) |
| POST | `/v1/posting/fbp/get` | Получить информацию об отправлении по идентификатору | [описание](https://docs.ozon.ru/api/seller/#operation/GetFbpPosting) |
| POST | `/v1/description-category/dependent-attributes` | Получить зависимые характеристики | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryDependentAttributes) |
| POST | `/v1/description-category/dependent-attributes/values` | Получить возможные значения дочерней характеристики | [описание](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryDependentAttributesValues) |
| POST | `/v1/analytics/local-sale/total` | Получить общую информацию о локальности продаж | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsLocalSaleTotal) |
| POST | `/v1/analytics/local-sale/clusters-items/info` | Получить информацию о локальности продаж по кластерам | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsLocalSaleClustersItemsInfo) |
| POST | `/v1/analytics/local-sale/items-clusters/info` | Получить информацию о локальности продаж товара по кластерам | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsLocalSaleItemsClustersInfo) |
| POST | `/v1/warehouse/rfbs/return-point/list` | Получить список пунктов возврата для склада rFBS | [описание](https://docs.ozon.ru/api/seller/#operation/WarehouseRfbsReturnPointList) |
| POST | `/v1/supply-order/shipment-plan-compliance/get` | Получить информацию о выполнении плана отгрузок | [описание](https://docs.ozon.ru/api/seller/#operation/SupplyOrderShipmentPlanComplianceGet) |
| POST | `/v1/return/box/get-by-barcode` | Получить информацию о возвратных коробках по штрихкоду с этикетки | [описание](https://docs.ozon.ru/api/seller/#operation/ReturnAPI_BoxGetByBarcode) |
| POST | `/v1/product/mismatches/list` | Получить несоответствия характеристик товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductMismatchesList) |
| POST | `/v1/report/finance/realization/list` | Получить список номеров отчётов о реализации товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ReportFinanceRealizationList) |
| POST | `/v1/report/finance/realization/number/create` | Получить идентификатор отчёта о реализации товаров по номеру | [описание](https://docs.ozon.ru/api/seller/#operation/CreateFinanceRealizationNumberReport) |
| POST | `/v1/report/finance/realization/number/posting/create` | Получить идентификатор позаказного отчёта о реализации товаров по номеру | [описание](https://docs.ozon.ru/api/seller/#operation/CreateFinanceRealizationNumberPostingReport) |
| POST | `/v1/review/first-reviews-collection/planned-product/activate` | Запустить запланированный сбор отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionPlannedProductActivate) |
| POST | `/v1/review/first-reviews-collection/product/add` | Добавить товары в сбор отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductAdd) |
| POST | `/v1/review/first-reviews-collection/product/delete` | Удалить товары из сбора отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductDelete) |
| POST | `/v1/review/first-reviews-collection/product/list` | Получить список товаров, которые участвуют в сборе отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductList) |
| POST | `/v1/review/first-reviews-collection/product/list-detailed` | Получить информацию о товарах в сборе отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductListDetailed) |
| POST | `/v1/review/first-reviews-collection/product/repeat` | Повторить сбор отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductRepeat) |
| POST | `/v1/review/first-reviews-collection/product/toggle` | Остановить или продолжить сбор отзывов | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductToggle) |
| POST | `/v1/review/first-reviews-collection/product/update-target` | Изменить цель по отзывам | [описание](https://docs.ozon.ru/api/seller/#operation/ReviewFirstReviewsCollectionProductUpdateTarget) |
| POST | `/v1/seller-actions/create/discount` | Создать акцию с механикой «Скидка» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscount) |
| POST | `/v1/seller-actions/create/discount-with-condition` | Создать акцию с механикой «Скидка от суммы заказа» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscountWithCondition) |
| POST | `/v1/seller-actions/create/installment` | Создать акцию с механикой «Беспроцентная рассрочка» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateInstallment) |
| POST | `/v1/seller-actions/create/multi-level-discount` | Создать акцию с механикой «Многоуровневая скидка от суммы» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateMultiLevelDiscount) |
| POST | `/v1/seller-actions/create/voucher` | Создать акцию с механикой «Скидка по промокоду» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateVoucher) |
| POST | `/v1/seller-actions/update/discount` | Обновить акцию с механикой «Скидка» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscount) |
| POST | `/v1/seller-actions/update/discount-with-condition` | Обновить акцию с механикой «Скидка от суммы заказа» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscountWithCondition) |
| POST | `/v1/seller-actions/update/installment` | Обновить акцию с механикой «Беспроцентная рассрочка» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateInstallment) |
| POST | `/v1/seller-actions/update/multi-level-discount` | Обновить акцию с механикой «Многоуровневая скидка от суммы» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateMultiLevelDiscount) |
| POST | `/v1/seller-actions/update/voucher` | Обновить акцию с механикой «Скидка по промокоду» | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateVoucher) |
| POST | `/v1/seller-actions/products/add` | Добавить товары в акцию | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsAdd) |
| POST | `/v1/seller-actions/products/candidates` | Получить список доступных для акции товаров | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsCandidates) |
| POST | `/v1/seller-actions/products/delete` | Удалить товары из акции | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsDelete) |
| POST | `/v1/seller-actions/products/list` | Получить список участвующих в акции товаров | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsList) |
| POST | `/v1/seller-actions/archive` | Перенести акцию в архив | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsArchive) |
| POST | `/v1/seller-actions/change-activity` | Включить или выключить акцию | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsChangeActivity) |
| POST | `/v1/seller-actions/list` | Получить список акций | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsList) |
| POST | `/v1/seller-actions/voucher/get` | Получить файл с промокодами в формате CSV | [описание](https://docs.ozon.ru/api/seller/#operation/SellerActionsVoucherGet) |
| POST | `/v1/actions/auto-add/products/list` | Получить список товаров из автодобавления в акцию Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsList) |
| POST | `/v1/actions/auto-add/products/candidates` | Получить список доступных товаров для автодобавления в акцию Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsCandidates) |
| POST | `/v1/actions/auto-add/products/delete` | Удалить товары из автодобавления в акцию Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsDelete) |
| POST | `/v1/actions/auto-add/products/update` | Добавить или обновить товары в автодобавлении в акцию Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsUpdate) |
| POST | `/v1/fbp/warehouse/list` | Получить список партнёрских складов | [описание](https://docs.ozon.ru/api/seller/#operation/FbpWarehouseList) |
| POST | `/v1/fbp/draft/get` | Получить информацию о черновике поставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftGet) |
| POST | `/v1/fbp/draft/list` | Список черновиков поставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftList) |
| POST | `/v1/fbp/draft/direct/seller-dlv/create` | Создать черновик с доставкой силами продавца | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectSellerDlvCreate) |
| POST | `/v1/fbp/draft/direct/seller-dlv/edit` | Обновить информацию о доставке силами продавца в черновике | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectSellerDlvEdit) |
| POST | `/v1/fbp/draft/direct/timeslot/edit` | Отредактировать таймслот в черновике | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectTimeslotEdit) |
| POST | `/v1/fbp/draft/direct/timeslot/get` | Получить список таймслотов для прямой поставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectGetTimeslot) |
| POST | `/v1/fbp/draft/direct/create` | Создать черновик заявки на поставку без указания способа доставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectCreate) |
| POST | `/v1/fbp/draft/direct/delete` | Удалить черновик заявки на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectDelete) |
| POST | `/v1/fbp/draft/direct/product/validate` | Проверить список товаров для склада партнёра | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectProductValidate) |
| POST | `/v1/fbp/draft/direct/registrate` | Перевести черновик в действующую поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDirectRegistrate) |
| POST | `/v1/fbp/draft/direct/tpl-dlv/create` | Создать черновик заявки на доставку сторонней транспортной компанией | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftDirectTplDlvCreate) |
| POST | `/v1/fbp/draft/direct/tpl-dlv/edit` | Редактировать черновик поставки со способом доставки сторонней транспортной компанией | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftDirectTplDlvEdit) |
| POST | `/v1/fbp/draft/drop-off/create` | Создать черновик для доставки в drop-off пункт | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffCreate) |
| POST | `/v1/fbp/draft/drop-off/delete` | Удалить черновик для доставки в drop-off пункт | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffDelete) |
| POST | `/v1/fbp/draft/drop-off/dlv/edit` | Отредактировать детали доставки для drop-off черновика | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffDlvEdit) |
| POST | `/v1/fbp/draft/drop-off/registrate` | Перевести черновик в действующую поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffRegistrate) |
| POST | `/v1/fbp/draft/drop-off/province/list` | Получить список провинций | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffProvinceList) |
| POST | `/v1/fbp/draft/drop-off/point/list` | Получить список drop-off пунктов в провинции | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffPointList) |
| POST | `/v1/fbp/draft/drop-off/point/timetable` | Получить расписание работы drop-off пункта | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffPointTimetable) |
| POST | `/v1/fbp/draft/drop-off/product/validate` | Проверить список товаров, которые склад партнёра может принять | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftDropOffProductValidate) |
| POST | `/v1/fbp/draft/pick-up/create` | Создать черновик заявки на pick-up поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftPickupCreate) |
| POST | `/v1/fbp/draft/pick-up/delete` | Отменить черновик заявки на pick-up поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftPickUpDelete) |
| POST | `/v1/fbp/draft/pick-up/dlv/edit` | Изменить черновик заявки на pick-up поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftPickupDlvEdit) |
| POST | `/v1/fbp/draft/pick-up/product/validate` | Провалидировать список товаров для pick-up поставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpDraftPickUpProductValidate) |
| POST | `/v1/fbp/draft/pick-up/registrate` | Перевести черновик в действующую поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpDraftPickUpRegistrate) |
| POST | `/v1/fbp/order/direct/cancel` | Отменить поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderDirectCancel) |
| POST | `/v1/fbp/order/direct/seller-dlv/edit` | Обновить информацию о доставке силами продавца | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderDirectSellerDlvEdit) |
| POST | `/v1/fbp/order/direct/tpl-dlv/edit` | Обновить информацию о доставке сторонней транспортной компанией | [описание](https://docs.ozon.ru/api/seller/#operation/FbpOrderDirectTplDlvEdit) |
| POST | `/v1/fbp/order/direct/timeslot/edit` | Отредактировать таймслот в заявке на поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpEditTimeslot) |
| POST | `/v1/fbp/order/direct/timeslot/list` | Получить список таймслотов для поставки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpAvailableTimeslotList) |
| POST | `/v1/fbp/order/drop-off/cancel` | Отменить поставку drop-off | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderDropOffCancel) |
| POST | `/v1/fbp/order/drop-off/dlv/edit` | Отредактировать информацию о поставке на drop-off пункт | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderDropOffDlvEdit) |
| POST | `/v1/fbp/order/drop-off/timetable` | Получить график работы drop-off пункта | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderDropOffTimetable) |
| POST | `/v1/fbp/order/pick-up/cancel` | Отменить pick-up поставку | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderPickUpCancel) |
| POST | `/v1/fbp/order/pick-up/dlv/edit` | Изменить данные о точке забора | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderPickUpDlvEdit) |
| POST | `/v1/fbp/act-from/create` | Сгенерировать акт приёмки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpCreateAct) |
| POST | `/v1/fbp/act-from/get` | Получить статус генерации акта приёмки | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpCheckActState) |
| POST | `/v1/fbp/act-to/create` | Сгенерировать транспортную накладную | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpCreateConsignmentNote) |
| POST | `/v1/fbp/act-to/get` | Получить статус генерации транспортной накладной | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpCheckConsignmentNoteState) |
| POST | `/v1/fbp/archive/get` | Получить информацию о завершённой поставке | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpArchiveGet) |
| POST | `/v1/fbp/archive/list` | Получить список завершённых поставок | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpArchiveList) |
| POST | `/v1/fbp/label/create` | Cоздать задание на генерацию этикеток | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpCreateLabel) |
| POST | `/v1/fbp/label/get` | Получить статус задания на генерацию этикеток | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpGetLabel) |
| POST | `/v1/fbp/order/get` | Получить информацию о конкретной поставке | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderGet) |
| POST | `/v1/fbp/order/list` | Получить список поставок | [описание](https://docs.ozon.ru/api/seller/#operation/FbpAPI_FbpOrderList) |
| POST | `/v1/posting/fbp/list` | Получить список отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/PostingFbpList) |
| POST | `/v1/carriage/container/create` | Создать грузоместо | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerCreate) |
| POST | `/v1/carriage/container/fill` | Наполнить грузоместо отправлениями | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerFill) |
| POST | `/v1/carriage/container/approve` | Подтвердить состав грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerApprove) |
| POST | `/v1/carriage/container/place-into` | Разместить коробки на палете | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerPlaceInto) |
| POST | `/v1/carriage/container/remove-postings` | Убрать отправления из грузоместа | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerRemovePostings) |
| POST | `/v1/carriage/container/remove-from` | Убрать коробки с палеты | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerRemoveFrom) |
| POST | `/v1/carriage/container/cancel` | Отменить грузоместо | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerCancel) |
| POST | `/v1/carriage/container/list` | Получить список грузомест | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerList) |
| POST | `/v1/carriage/container/get` | Получить информацию о грузоместах | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerGet) |
| POST | `/v1/carriage/container/status/get` | Получить статус грузомест FBS | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerStatusGet) |
| POST | `/v1/carriage/container/task/info` | Получить статус задачи грузового места | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerTaskInfo) |
| POST | `/v1/carriage/container/document/get` | Получить документы по грузоместам — ТрН и лист отгрузки | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerDocumentGet) |
| POST | `/v1/carriage/container/label/get` | Получить этикетку по грузоместам | [описание](https://docs.ozon.ru/api/seller/#operation/CarriageContainerLabelGet) |
| POST | `/v1/chat/send/message` | Отправить сообщение | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatSendMessage) |
| POST | `/v1/chat/start` | Создать новый чат | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatStart) |
| POST | `/v2/chat/read` | Отметить сообщения как прочитанные | [описание](https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatReadV2) |
| POST | `/v1/analytics/data` | Данные аналитики | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsGetData) |
| POST | `/v1/analytics/product-queries` | Получить информацию о запросах моих товаров | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueries) |
| POST | `/v1/analytics/product-queries/details` | Получить детализацию запросов по товару | [описание](https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueriesDetails) |
| POST | `/v1/finance/realization/by-day` | Отчёт о реализации товаров за день | [описание](https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetRealizationByDayReportV1) |
| POST | `/v1/search-queries/text` | Получить список поисковых запросов по тексту | [описание](https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesText) |
| POST | `/v1/search-queries/top` | Получить список популярных поисковых запросов | [описание](https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesTop) |
| POST | `/v1/product/prices/details` | Получить подробную информацию о ценах товаров | [описание](https://docs.ozon.ru/api/seller/#operation/ProductPricesDetails) |
| POST | `/v1/cancel-reason/list` | Причины отмены отправлений | [описание](https://docs.ozon.ru/api/seller/#operation/CancelReasonList) |
| POST | `/v1/cancel-reason/list-by-order` | Причины отмены заказа | [описание](https://docs.ozon.ru/api/seller/#operation/CancelReasonListByOrder) |
| POST | `/v1/cancel-reason/list-by-posting` | Причины отмены отправления | [описание](https://docs.ozon.ru/api/seller/#operation/CancelReasonAPI_CancelReasonListByPosting) |
| POST | `/v1/delivery/check` | Проверить доступность доставки для покупателя Deprecated | [описание](https://docs.ozon.ru/api/seller/#operation/DeliveryCheck) |
| POST | `/v2/delivery/checkout` | Получить доступные варианты доставки | [описание](https://docs.ozon.ru/api/seller/#operation/DeliveryCheckout) |
| POST | `/v1/delivery/map` | Отрисовать точки на карте | [описание](https://docs.ozon.ru/api/seller/#operation/DeliveryMap) |
| POST | `/v1/delivery/point/info` | Получить информацию о точке самовывоза | [описание](https://docs.ozon.ru/api/seller/#operation/DeliveryPointInfo) |
| POST | `/v1/delivery/point/list` | Получить список точек самовывоза | [описание](https://docs.ozon.ru/api/seller/#operation/DeliveryAPI_DeliveryPointList) |
| POST | `/v1/order/cancel` | Отменить заказ | [описание](https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancel) |
| POST | `/v1/order/cancel/check` | Проверить возможность отмены заказа | [описание](https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancelCheck) |
| POST | `/v1/order/cancel/status` | Получить статус отмены заказа | [описание](https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancelStatus) |
| POST | `/v2/order/create` | Создать заказ | [описание](https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCreate) |
| POST | `/v1/order/code/get` | Получить код выдачи заказа | [описание](https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCodeGet) |
| POST | `/v1/posting/cancel` | Отменить отправление из заказа | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingCancel) |
| POST | `/v1/posting/cancel/status` | Проверить статус отмены отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingCancelStatus) |
| POST | `/v1/posting/marks` | Получить маркировки экземпляров из отправления | [описание](https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingMarks) |
