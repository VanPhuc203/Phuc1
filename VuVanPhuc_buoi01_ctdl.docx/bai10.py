def decimal_to_binary(n):
    # Nếu số là 0, trả về chuỗi rỗng
    if n == 0:
        return ""
    else:
        # Chia số cho 2 và ghép phần dư vào kết quả
        return decimal_to_binary(n // 2) + str(n % 2)

# Nhập một số nguyên từ người dùng
decimal_number = int(input("Nhập một số nguyên hệ thập phân: "))

# Kiểm tra xem số nhập vào có là số nguyên không âm không
if decimal_number < 0:
    print("Nhập một số nguyên không âm.")
else:
    # Gọi hàm để chuyển đổi số sang hệ nhị phân
    binary_result = decimal_to_binary(decimal_number)

    # In kết quả ra màn hình
    print(f"{decimal_number} ở hệ nhị phân là: {binary_result}")
