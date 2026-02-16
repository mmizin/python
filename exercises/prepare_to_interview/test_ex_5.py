# def get_users(page: int, page_size: int) -> dict:
#     """
#     Returns:
#     {
#         "items": [{"id": int, "email": str, "is_active": bool}],
#         "total": int
#     }
#     """
#     ...

from math import ceil
from collections import Counter


def get_users(page: int, page_size: int) -> dict:
    ...


def validate_page_size(page_size: int, users: list[dict], total_pages: int, current_page: int) -> list[str]:
    errors = []
    
    if total_pages == current_page:
        if page_size <= len(users):
            errors.append(f"Page size mismatch on page {current_page}.Total users: {len(users)}.")
    elif page_size > len(users):
        errors.append(f"Page size mismatch on page {current_page}.Total users: {len(users)}.")
    
    return errors

def validate_ids_are_unique(users: list[dict]) -> list[str]: # [{"id": int, "email": str, "is_active": bool}]
    errors = []
    ids = [user["id"] for user in users]
    duplicated_ids = [{k: v} for k, v in Counter(ids).items() if v > 1]
    
    if duplicated_ids:
        for item in duplicated_ids:
            errors.append(f"The ID: {user_id} duplicates -> {times}\nUsers: {[user for user in users if user['id'] == user_id]}" for user_id, times in item.items())
    
    return errors


def validate_emails_are_unique(users: list[dict]) -> list[str]:  # [{"id": int, "email": str, "is_active": bool}]
    errors = []
    ids = [user["email"] for user in users]
    duplicated_ids = [{k: v} for k, v in Counter(ids).items() if v > 1]
    
    if duplicated_ids:
        for item in duplicated_ids:
            errors.append(f"The EMAIL: {email} duplicates -> {times}\nUsers: {[user for user in users if user['email'] == email]}" for email, times in item.items())
    
    return errors

def validate_user_is_active(users: list[dict]):
    errors = []
    
    for user in users:
        if not user["is_active"]:
            errors.append(f"User with id: {user['id']} is inactive.")
        
    return errors


def test_validate_users():
    page_size = 100
    users = []
    start_page = 1
    errors_obj = {"errors": {
        "page_size_errors": [],
        "total_users_count_errors": [],
        "unique_ids_errors": [],
        "unique_emails_errors": [],
        "is_active_user_errors": []}
    }
    
    response = get_users(start_page, page_size)
    users += response["items"]
    total_users = response["total"]
    total_pages = ceil(total_users / page_size)
    
    errors_obj["errors"]["page_size_errors"] += validate_page_size(page_size, users, total_pages, start_page)
    
    for page in range(start_page + 1, total_pages + 1):
        response = get_users(page, page_size)
        users += response["items"]
        errors_obj["errors"]["page_size_errors"] += validate_page_size(page_size, response["items"], total_pages, page)
    
    if total_users != len(users):
        errors_obj["errors"]["total_users_count_errors"].appemd(f"Total users count mismatch."
                                                      f"E\nxpected: {total_users}"
                                                      f"\nActual: {len(users)}")
    
    errors_obj["errors"]["unique_ids_errors"] = validate_ids_are_unique(users)
    errors_obj["errors"]["unique_emails_errors"] = validate_emails_are_unique(users)
    
    
    for error_values in errors_obj["errors"].values():
        assert not error_values, f"Errors found: {errors_obj}"
        