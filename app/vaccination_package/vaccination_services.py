def validate_keys(payload: dict, expected_keys: set):

    body_keys = set(payload.keys())
    
    invalid_keys = body_keys - expected_keys

    if invalid_keys:
        raise KeyError(
            {
                "error": "invalid_keys",
                "expected": list(expected_keys),
                "wrong_key(s)": list(invalid_keys)
            }
        )

    for key in body_keys:
        if type(key) != str:
            raise KeyError(
            {"error": "All keys must be strings"}
        )    
