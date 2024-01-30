def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
string1 = "racecar"
string2 = "hello"
print(is_palindrome(string1))  
print(is_palindrome(string2))  