def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merge_dicts(dict1, dict2)
print(merge_dicts(dict1, dict2))