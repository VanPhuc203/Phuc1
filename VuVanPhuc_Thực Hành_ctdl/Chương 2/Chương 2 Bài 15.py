def DayConDaiNhat(b):
    set_b = set(b)

    max_length = 0
    max_subarray = []
    current_length = 0
    current_subarray = []

    for i in range(len(a)):
        if a[i] in set_b:
            current_length += 1
            current_subarray.append(a[i])
        else:
            if current_length > max_length:
                max_length = current_length
                max_subarray = current_subarray

            current_length = 0
            current_subarray = []

    return max_subarray

a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
result = DayConDaiNhat(b)
print("Dãy con chung đầu tiên có chiều dài lớn nhất:", result)
