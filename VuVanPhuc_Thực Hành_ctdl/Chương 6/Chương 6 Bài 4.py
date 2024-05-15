def Hop(a, b):
    # Tạo một tập hợp từ hai mảng a và b
    c = set(a + b)
    # Chuyển đổi tập hợp thành danh sách và sắp xếp
    c = sorted(list(c))
    return c

# Ví dụ:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hop(a, b)
print(c)  # Kết quả: [1, 2, 3, 4, 5, 6, 7, 8, 9]
