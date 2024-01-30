# : Đây là chuỗi ban đầu mà chúng ta sẽ thao tác.
a = 'spam-spam-spam'
# Đây là ký tự mà chúng ta sẽ sử dụng để tách chuỗi a.
delimiter = 'a'
# Phương thức split tách chuỗi a thành một danh sách các chuỗi nhỏ hơn, với delimiter là ký tự được sử dụng để xác định nơi tách. Kết quả được lưu vào biến b.
b = a.split(delimiter)
# In ra danh sách b
print(b)
# Phương thức join ghép các phần tử của danh sách b thành một chuỗi, với delimiter là ký tự được chèn giữa mỗi phần tử. Kết quả được in ra. Trong trường hợp này, kết quả sẽ là chuỗi ban đầu spam-spam-spam.
print(delimiter.join(b))