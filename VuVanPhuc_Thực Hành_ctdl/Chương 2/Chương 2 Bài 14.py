def DayConDauTien(b):
 
    set_b = set(b)

    for i in range(len(a)):
        if a[i] in set_b:
            j = i
            while j < len(a) and a[j] in set_b:
                j += 1
            return a[i:j]

    return []

a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
result = DayConDauTien(b)
print("Dãy con chung đầu tiên:", result)
