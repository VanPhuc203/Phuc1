def factorial(n):
    # Gọi assert để kiểm tra xem n có phải là số nguyên dương không.
    assert n >= 0 and int(n) == n
    # Sử dụng int(n) == n để kiểm tra xem n có phải là số nguyên không.
    if n in [0,1]:
        # Nếu n là 0 hoặc 1, hàm trả về 1 vì giai thừa của 0 và 1 là 1.
        return 1
    else:
        # Nếu n lớn hơn 1, hàm gọi lại chính nó với tham số n - 1.
        return n * factorial(n-1)
# Người dùng nhập một số nguyên dương.
num = int(input("Nhập một số nguyên dương: "))
result = factorial(num)
# Hàm tính giai thừa của số đó và in kết quả ra màn hình.
print(result)