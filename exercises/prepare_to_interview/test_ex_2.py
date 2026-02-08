
"""
Given

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

Test should verify that:

Each order has required fields

id

amount

Order id is a positive integer

Order amount is a positive number

👉 You may assume pagination works correctly
👉 Focus only on data validation, not pagination logic
👉 Use Pytest assertions (no extra frameworks)
"""
from math import ceil
from typing import NoReturn


def fetch_orders(page: int, page_size: int) -> dict:
    ...

def validate_required_fields_present(orders: list[dict], properties: list[str]) -> list[str]:
    errors = []
    
    for order in orders:
            for prop in properties:
                if prop not in order.keys():
                    errors.append(f"\nMissing required property '{prop}' in order -> {order}")
    
    return errors

def validate_order_values_positive_numbers(orders: list[dict]) -> list[str]:
    errors = []
    
    for order in orders:
        if not isinstance(order["id"], int) or order['id'] <= 0:
            errors.append(f"\nInvalid value for order: {order}. Order id must be a positive integer.")
        
        if not isinstance(order["amount"], (int, float)) or order['amount'] <= 0:
            errors.append(f"\nInvalid value for order: {order}. Order amount must be a positive number.")
    
    return errors
    
    

def test_fetch_orders_data_validation():
    response = fetch_orders(1, 1000)
    orders = response["items"]
    
    required_filed_errors = validate_required_fields_present(orders, ["id", "amount"])
    positive_values_errors = validate_order_values_positive_numbers(orders)
    
    assert not required_filed_errors and not positive_values_errors, "".join(required_filed_errors + positive_values_errors)
    