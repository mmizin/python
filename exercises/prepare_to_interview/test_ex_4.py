def fetch_orders(page: int, page_size: int) -> dict:
    """
    Returns:
    {
        "items": [{"id": int, "amount": int}, ...],
        "total": int  # total orders in the system
    }
    """
    ...


from math import ceil
from collections import Counter


def test_validate_fetch_orders_response():
    page_size = 10
    start_page = 1
    orders = []
    
    response = fetch_orders(start_page, page_size)
    total_orders = response.get("total")
    orders += response.get("items")
    total_pages = ceil(total_orders / page_size)
    
    for page in range(start_page + 1, total_pages + 1):
        response = fetch_orders(page, page_size)
        orders += response.get("items")
    
    assert len(orders) == total_orders, (f"Orders coount mismatch."
                                         f"\nExpected orders: {total_orders}"
                                         f"\nActual orders: {len(orders)}")
    
    order_ids = [order["id"] for order in orders]
    duplicates = [order_id for order_id, count in Counter(order_ids).items() if count > 1]
    
    assert not duplicates, f"Duplicates found: {duplicates}"


def generate_keys(batch_size: int) -> list[str]:
    """
    Returns a list of unique license keys, each 16 chars long
    """
    ...


def test_validate_key_generation():
    batch_size = 100
    key_length = 16
    keys = generate_keys(batch_size)
    
    assert len(keys) == batch_size, f"Expected {batch_size} keys, got {len(keys)}"
    
    duplicates = {k: v for k, v in Counter(keys).items() if v > 1}
    assert not duplicates, ("Duplicates found:"
                            + "\n".join([f"Key: {key} duplicated {value} times" for key, value in duplicates.items()]))
    
    keys_with_wrong_length = [key for key in keys if len(key) < key_length or len(key) > key_length]
    assert not keys_with_wrong_length, (f"Keys with wrong length found"
                                        + "\n".join([f"Key: {key} has length {len(key)}"
                                                     for key in keys_with_wrong_length]))


def get_orders_from_api() -> list[dict]: ...


def get_orders_from_db() -> list[dict]: ...


def test_compare_orders_sources():
    orders_from_api = get_orders_from_api()
    orders_from_db = get_orders_from_db()
    
    # API и база возвращают одинаковое количество заказов
    assert len(orders_from_api) == len(orders_from_db), (f"Orders count mismatch."
                                                         f"\nAPI orders count: {len(orders_from_api)}"
                                                         f"\nDB orders count: {len(orders_from_db)}")
    
    # Все id совпадают + Нет пропущенных заказов
    orders_from_api.sort(key=lambda order: order["id"])
    orders_from_db.sort(key=lambda order: order["id"])
    assert orders_from_api == orders_from_db, (f"Orders are not the same."
                                               f"\nAPI orders: {orders_from_api}"
                                               f"\nDB orders: {orders_from_db}")
    
    order_ids = [order["id"] for order in orders_from_api]
    duplicates = {k: v for k, v in Counter(order_ids).items() if v > 1}
    assert not duplicates, f"Duplicates are found: {duplicates}"



