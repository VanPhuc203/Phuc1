def factorial(n):
    # Nếu n là số âm, hàm trả về -1
    if n < 0:
        return -1
    # Nếu n bằng 0, hàm trả về 1, vì giai thừa của 0 là 1.
    elif n == 0:
        return 1
    # Nếu n không âm và không bằng 0, hàm sử dụng đệ quy để tính giai thừa của n bằng cách nhân n với giai thừa của (n-1).
    else:
        return n * factorial(n-1)
# hàm factorial được gọi với đối số 5 và kết quả được in ra.
print(factorial(5))