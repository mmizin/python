def merge_dicts(dict1, dict2):
    new_dict = {k: v for k, v in dict2.items() if k not in dict1}
    
    for k, v in dict1.items():
        if not k in dict2:
            new_dict[k] = v
        elif isinstance(v, int) and isinstance(dict2[k], int):
            new_dict[k] = v + dict2[k]
        else:
            new_dict[k] = dict2[k]
        
    return new_dict


d1 = {"i": 7, "a": 111, "b": 2, "c": 3, "e": 5}
d2 = {"a": 11, "b": 2, "c": 33, "d": 4}
print(merge_dicts(d1, d2))

def merge_dicts(dest: dict, source: dict) -> dict:

    for k, v in source.items():
        dest[k] = v

    return dest

print(merge_dicts(d1, d2))

def merge_dicts(dest: dict, source: dict) -> dict:

    return dest | source

print(merge_dicts(d1, d2))

def merge_dicts(dest: dict, source: dict) -> dict:

    return {**dest, **source}

print(merge_dicts(d1, d2))








