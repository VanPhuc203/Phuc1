def check_same_frequency(list1, list2):
    frequency_dict1 = {item: list1.count(item) for item in set(list1)}
    frequency_dict2 = {item: list2.count(item) for item in set(list2)}

    return frequency_dict1 == frequency_dict2

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

print(check_same_frequency(list1, list2))