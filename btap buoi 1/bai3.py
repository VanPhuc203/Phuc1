def recursiveMethod(n):
    # Điều kiện kiểm tra nếu n nhỏ hơn 1.
    if n<1:
        # Nếu n thỏa mãn điều kiện (nhỏ hơn 1), một thông điệp "n is less than 1" sẽ được in ra màn hình.
        print("n is less than 1")
    else:
        # Hàm recursiveMethod được gọi lại với tham số là n-1. Điều này tạo ra một cuộc gọi đệ quy, nghĩa là hàm sẽ gọi chính nó với một giá trị nhỏ hơn cho đến khi n thỏa mãn điều kiện n < 1.
        recursiveMethod(n-1)
        # Xuất n
        print(n)
# Nhập dữ liệu từ người dùng bằng hàm Input
num = int(input())
recursiveMethod(num)