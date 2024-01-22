def foo(array):
    # biến để lưu trữ tổng các phần tử trong mảng
    sum = 0
    # biến để lưu trữ tích các phần tử trong mảng
    product = 1
    #duyệt qua từng phần tử i trong mảng array và cộng giá trị của i vào biến sum.
    for i in array:
         sum += i
    #duyệt qua từng phần tử i trong mảng array và nhân giá trị của i vào biến product.
    for i in array:
        product *= i
    # in ra tổng và tích đã tính được, sử dụng hàm print và chuyển đổi các giá trị sum và product thành chuỗi bằng cách sử dụng str()
    print("Sum = "+str(sum)+", Product = "+str(product))
    #Hàm foo được gọi với đối số là một mảng [1, 2, 3, 4].
foo([1,2,3,4])