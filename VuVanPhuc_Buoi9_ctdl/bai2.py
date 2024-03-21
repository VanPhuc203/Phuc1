def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k-1)

def neper(n):
    if n < 0:
        raise ValueError("Số nguyên phải lớn hơn hoặc bằng 0")
    else:
        sum_e = sum(1/factorial(k) for k in range(n+1))
        return sum_e

num = 6
result = neper(num)
print(f"Tổng của a0 + a1 + ... + a{num} là: {result}")
