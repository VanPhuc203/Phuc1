
import array 
# Tạo một mảng số nguyên my_array1 với giá trị ban đầu là [1, 2, 3, 4].
my_array1= array.array('i', [1,2,3,4] )   
# arr là mảng cần tìm kiếm và target là giá trị cần tìm trong mảng
def linear_search(arr,target):
    # sử dụng vòng lặp for để duyệt qua từng phần tử trong mảng
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#Gọi hàm linear_search với my_array1 là mảng cần tìm kiếm và 8
print(linear_search(my_array1, 8))