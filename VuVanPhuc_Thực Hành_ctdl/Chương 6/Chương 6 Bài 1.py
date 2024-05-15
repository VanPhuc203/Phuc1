def Duynhat(a):
    # Sử dụng set để loại bỏ các phần tử trùng lặp
    b = list(set(a))
    # Sắp xếp mảng b theo thứ tự tăng dần
    b.sort()
    return b

# Ví dụ:
a = [1, 5, 3, 7, 5, 9, 7]
print(Duynhat(a))  # Kết quả: [1, 3, 5, 7, 9]
