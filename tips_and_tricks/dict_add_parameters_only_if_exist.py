def some_function(
    user,
    user_id = None
    
) -> dict:
    payload = {
       "user": user,
        **({"userId": user_id} if user_id else {}),
    }
    return payload