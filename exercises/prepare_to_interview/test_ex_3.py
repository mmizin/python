"""
Given:

API method:

def fetch_orders(page: int, page_size: int) -> dict:
    Returns:
    {
        "items": [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200}
        ],
        "total": 5
    }


Test requirements:

Verify that page_size parameter is respected

No page should return more than page_size items

The last page may contain fewer

Verify that empty pages behave correctly

Requesting page beyond total returns an empty list

Verify that all orders are unique by id across all pages

Constraints:

Use pytest only, no extra frameworks

Pagination is real (assume multiple pages)

Focus on robustness / edge cases

API may return total != sum of items if misconfigured — catch it

🔑 Bonus points (Apple-style interview flavor):

Make test fail fast if a page is malformed

Print which page caused the problem

Avoid infinite loops if fetch_orders misbehaves
"""
import random
from math import ceil
from collections import Counter


def fetch_orders(page: int, page_size: int) -> dict:
    ...

def validate_page_order_count(page_size: int, orders: list[dict], page_number: int, total_pages: int):
    
    if page_number < total_pages:  #The last page may contain a fewer so don't check it'
        assert len(orders) <= page_size, (f"Orders count mismatch on page {page_number}."
                                          f"\nExpected orders count: {page_size}, Actual orders count: {len(orders)}")
    elif page_number == total_pages:
        assert len(orders) <= page_size, (f"Orders count mismatch on page {page_number}."
                                          f"\nExpected orders count: <= {page_size}, Actual orders count: {len(orders)}")
    

def test_fetch_orders():
    page_size = 100
    orders = []
    start_page = 1
    
    response = fetch_orders(start_page, page_size)
    orders += response["items"]
    total_orders = response["total"]
    pages = ceil(total_orders / page_size)
    
    # Verify that page_size parameter is respected
    validate_page_order_count(page_size, orders, start_page, pages)
    
    for page in range(start_page + 1, pages + 1):
        # Verify that page_size parameter is respected
        response = fetch_orders(page, page_size)
        items = response["items"]
        validate_page_order_count(page_size, items, page, pages)
        orders += items
    
    assert len(orders) == total_orders, (f"Orders count mismatch."
                                         f"\nActual order count: {len(orders)}, Expected order count: {total_orders}")
    
    # Verify that all orders are unique by id across all pages
    order_ids = [order["id"] for order in orders]
    duplicated_orders = [order_id for order_id, amount in Counter(order_ids).items() if amount > 1]
    assert not duplicated_orders, f"Duplicate orders found: {duplicated_orders}"
    
    # Requesting page beyond total returns an empty list
    response = fetch_orders(pages + random.randint(1, 100), page_size)
    assert response["items"] == [], f"Empty list expected for items, but got: {response['items']}"