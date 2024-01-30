# danh sách mà chúng ta sẽ tìm kiếm mục tiêu
myList = [10,20,30,40]
# Định nghĩa hàm linear_search với hai tham số: list (danh sách cần tìm kiếm) và target (mục tiêu cần tìm).
def linear_search(list, target):
    # Duyệt qua từng phần tử trong danh sách. enumerate trả về cả chỉ số (index) và giá trị của mỗi phần tử.
    for index, value in enumerate(list):
        # Nếu giá trị của phần tử hiện tại bằng mục tiêu, hàm sẽ trả về chỉ số của phần tử đó.
        if value == target:
            return index
    # Nếu không tìm thấy mục tiêu trong danh sách, hàm sẽ trả về -1.
    return -1
# Gọi hàm linear_search với myList và mục tiêu là 50, sau đó in kết quả. Trong trường hợp này, vì 50 không tồn tại trong danh sách, đầu ra sẽ là -1.
print(linear_search(myList,target=50))