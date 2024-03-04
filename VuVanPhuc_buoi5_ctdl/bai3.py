def max_value_key(my_dict):
    if not my_dict:
        return None

    # Tìm kí tự có giá trị lớn nhất bằng max() và tham số kí tự
    max_key = max(my_dict, key=my_dict.get)
    return max_key

# Example usage:
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)
print(max_value_key(my_dict))