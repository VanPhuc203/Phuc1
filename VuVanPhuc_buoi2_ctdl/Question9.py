def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    # Nếu n không lớn hơn 0, hàm trả về 0.
    if n <= 0:
        return 0
    # Nếu n bằng 1, hàm trả về 1.
    elif n == 1:
        return 1
    # Nếu n lớn hơn 1, hàm sử dụng đệ quy để tính giá trị Fibonacci cho n bằng cách cộng giá trị Fibonacci của (n-1) và (n-2).
    return fib(n-1) + fib(n-2)
#  hàm allFib được gọi với đối số 20, nghĩa là sẽ in ra giá trị của dãy Fibonacci cho các số từ 0 đến 19.
allFib(20)