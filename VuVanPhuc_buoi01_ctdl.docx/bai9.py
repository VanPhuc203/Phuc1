def gcd(a, b):
    # Nếu b là 0, GCD là a
    if b == 0:
        return a
    else:
        # GCD(a, b) = GCD(b, a % b)
        return gcd(b, a % b)

# Nhập hai số nguyên dương từ người dùng
num1 = int(input("Nhập số nguyên dương thứ nhất: "))
num2 = int(input("Nhập số nguyên dương thứ hai: "))

# Kiểm tra xem cả hai số đều là số nguyên dương
if num1 <= 0 or num2 <= 0:
    print("Nhập hai số nguyên dương.")
else:
    # Tính GCD sử dụng hàm đệ quy
    result = gcd(num1, num2)

    # In kết quả ra màn hình
    print(f"GCD của {num1} và {num2} là {result}")
