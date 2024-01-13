# Hàm sum_of_digits nhận một số nguyên n làm đầu vào.
def sum_of_digits(n):
    # Nếu n là một chữ số (nhỏ hơn 10), hàm trả về chính số đó.
    if n < 10:
        return n
    else:
        # Hàm tính tổng của chữ số cuối cùng (n % 10) và tổng các chữ số của phần còn lại của số (n // 10).
        return n % 10 + sum_of_digits(n // 10)

# Lấy dữ liệu từ người dùng 
num = int(input("Nhập một số nguyên dương: "))

# Kiểm tra nếu đầu vào là số nguyên dương
if num <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    # Tính tổng các chữ số bằng cách sử dụng hàm đệ quy
    result = sum_of_digits(num)
    print(result)
