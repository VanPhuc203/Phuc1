import array 
# Tạo một mảng rỗng (my_array) với kiểu dữ liệu là 'i' (kiểu số nguyên).
my_array = array .array('i')
# In ra mảng rỗng vừa tạo.
print(my_array)
# Tạo một mảng (my_array1) với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4].
my_array1 = array.array('i', [1,2,3,4])
# In ra mảng này
print(my_array1)
# Import thư viện numpy và đặt tên ngắn là np.
import numpy as np
# Tạo một mảng rỗng (np_array) với kiểu dữ liệu là int
np_array = np.array([], dtype=int)
# In ra mảng rỗng vừa tạo.
print(np_array)
# Tạo một mảng (np_array1) với giá trị khởi tạo là [1, 2, 3, 4].
np_array1 = np.array([1,2,3,4])
# In ra mảng
print(np_array1)