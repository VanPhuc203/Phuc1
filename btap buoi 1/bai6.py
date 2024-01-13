def fibonacci(n):
    # Kiểm tra n là số nguyên không âm
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    # Số Fibonacci của 0 và 1 là chính nó
    if n in [0,1]:
        return n
    else:
        # Bước đệ quy: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)
# Người dùng nhập một số nguyên dương
num = int(input("Nhập một số nguyên dương: "))
# Tính số Fibonacci của số nguyên đó và in kết quả ra màn hình
result = fibonacci(num)
print(result)
