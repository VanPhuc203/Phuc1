def powerOfTwo(n):
    # Kiểm tra nếu n bằng 0
    if n == 0:
        # Nếu điều kiện trên đúng, hàm trả về giá trị 1. Điều này phản ánh rằng 2^0 = 1.
        return 1
    else:
        # Hàm gọi lại chính nó với tham số n-1
        power = powerOfTwo(n-1)
        # Hàm trả về giá trị là lũy thừa của 2 (2^k) với k là giá trị trả về từ cuộc gọi đệ quy, nhân với 2.
        return power * 2
# Nhập một số nguyên từ người dùng và lưu vào biến num
num =int(input())
# Gọi hàm powerOfTwo với tham số là num và lưu kết quả vào biến a.
a = powerOfTwo(num)
# In ra màn hình giá trị của a
print(a)