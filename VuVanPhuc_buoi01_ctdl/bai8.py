def power(base, exponent):
    # Lũy thừa của số 0 là 1
    if exponent == 0:
        return 1
    else:
        # Bước đệ quy: power(base, exponent) = base * power(base, exponent-1)
        return base * power(base, exponent - 1)

# Nhập giá trị cơ sở (base) và số mũ (exponent) từ người dùng
base = float(input("Nhập giá trị cơ sở (base): "))
exponent = int(input("Nhập số mũ (exponent): "))

# Tính lũy thừa sử dụng hàm đệ quy
result = power(base, exponent)

# In kết quả ra màn hình
print(f"{base}^{exponent} = {result}")
