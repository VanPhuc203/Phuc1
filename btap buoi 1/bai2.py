# Đây là định nghĩa của hàm firstMethod(). Hàm này gọi hàm secondMethod() và sau đó in ra một thông điệp "I am the first Method". 
def firstMethod():
    secondMethod()
    print("I am the first Method")
# Đây là định nghĩa của hàm secondMethod(). Hàm này gọi hàm thirdMethod() và sau đó in ra một thông điệp "I am the second Method".
def secondMethod():
    thirdMethod()
    print("I am the second Method")
# Đây là định nghĩa của hàm thirdMethod(). Hàm này gọi hàm fourthMethod() và sau đó in ra một thông điệp "I am the third Method".    
def thirdMethod():
    fourthMethod()
    print("I am the third Method")
# Đây là định nghĩa của hàm fourthMethod(). Hàm này chỉ đơn giản in ra một thông điệp "I am the fourth Method".
def fourthMethod():
    print("I am the fourth Method")
# Khi hàm này được gọi, nó bắt đầu thực thi từ đầu và kết quả là nó sẽ gọi lần lượt các hàm khác nhau theo chuỗi.
firstMethod()