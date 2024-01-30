# danh sách mà chúng ta sẽ tìm kiếm mục tiêu
myList = [10, 20, 30, 40, 50, 60, 70]
# giá trị mục tiêu mà chúng ta muốn tìm trong danh sách.
target = 50
# Kiểm tra xem mục tiêu có tồn tại trong danh sách hay không. Nếu có, thực hiện khối lệnh sau đó.
if target in myList:
    # Nếu mục tiêu tồn tại trong danh sách, in ra thông báo rằng mục tiêu nằm trong danh sách.
    print(f"{target} is in the list")
# Nếu mục tiêu không tồn tại trong danh sách, in ra thông báo rằng mục tiêu không nằm trong danh sách.
else:
    print(f"{target}is not in the list")