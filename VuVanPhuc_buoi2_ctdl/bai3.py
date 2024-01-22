import array 

# Tạo một mảng có tên my_array1 chứa các số nguyên ('i') với giá trị ban đầu là [1, 2, 3, 4].
my_array1 = array.array('i', [1,2,3,4])
# In ra mảng my_array1. Kết quả sẽ là [1, 2, 3, 4].
print(my_array1)
# Thêm số 6 vào vị trí đầu tiên của mảng my_array1. Phương thức insert nhận hai đối số, đối số đầu tiên là vị trí cần chèn
my_array1.insert(0,6)
# sau khi đã thêm số 6 vào vị trí đầu tiên. Kết quả sẽ là [6, 1, 2, 3, 4].
print(my_array1)