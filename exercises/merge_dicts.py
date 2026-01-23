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
