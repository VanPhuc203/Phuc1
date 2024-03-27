
def sum_of_divisors(n):
    """Calculate the sum of divisors of a number."""
    return sum([i for i in range(1, n) if n % i == 0])

def classify_number(n):
    """Classify a number as deficient, perfect, or abundant."""
    s = sum_of_divisors(n)
    if s < n:
        return 'deficient'
    elif s == n:
        return 'perfect'
    else:
        return 'abundant'

def number(x, y):
    """Print the classification of numbers from x to y."""
    for i in range(x, y + 1):
        classification = classify_number(i)
        print(f"Number {i} is {classification}.")

x = 6
y = 12
number(x, y)