def reverse_integer(num):
    reversed_num = 0
    is_negative = False

    if num < 0:
        is_negative = True
        num = -num

    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10

    if is_negative:
        reversed_num = -reversed_num

    return reversed_num

num1 = 1234
print(reverse_integer(num1))  
