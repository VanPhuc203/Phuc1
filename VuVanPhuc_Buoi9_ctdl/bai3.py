def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def gcd_non_recursive(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = 372
n = 84
print(f"GCD đệ quy của {m} và {n} là: {gcd_recursive(m, n)}")
print(f"GCD không đệ quy của {m} và {n} là: {gcd_non_recursive(m, n)}")
