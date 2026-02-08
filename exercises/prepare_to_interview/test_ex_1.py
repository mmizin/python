"""
🎯 Task
Part 1

Write a Pytest test that:

Retrieves all orders from all pages

Verifies that:

the number of retrieved orders equals total

there are no duplicate orders by id

👉 You may assume that fetch_orders is already implemented and works correctly.
    def fetch_orders(page: int, page_size: int) -> dict:
        Returns:
        {
            "items": [
                {"id": 1, "amount": 100},
                {"id": 2, "amount": 200}
            ],
            "total": 5
        }
"""

from math import ceil
from collections import Counter

def test_retrieve_all_orders(admin_user):
    page_size = 100
    orders = []
    start_page = 1
    
    response = admin_user['api'].fetch_orders(start_page, page_size)
    total_orders_count = response['total']
    orders += response['items']
    pages = ceil(total_orders_count / page_size)
    
    if pages:
        for page in range(start_page + 1, pages + 1):
            response = admin_user['api'].fetch_orders(page, page_size)
            orders += response['items']
    
    assert len(orders) == total_orders_count, (f"Orders count mismatch."
                                               f"\nActual order count: {len(orders)} "
                                               f"!= Expected order count {total_orders_count}")
    
    id_counter = Counter([order["id"] for order in orders])
    duplicates = [id for id, count in id_counter.items() if count > 1]
    assert not duplicates, f"Duplicate orders found: {duplicates}"
    