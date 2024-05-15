def Giao(a, b):
    # Chuyển đổi mảng a và b thành set để loại bỏ các phần tử trùng lặp
    set_a = set(a)
    set_b = set(b)
    # Tìm các phần tử đồng thời có trong a và b
    c = list(set_a & set_b)
    # Sắp xếp mảng c theo thứ tự tăng dần
    c.sort()
    return c

# Ví dụ:
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print(Giao(a, b))  # Kết quả: [2, 3, 9]
