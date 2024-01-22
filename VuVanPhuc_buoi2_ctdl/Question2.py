def printPairs(array):
    # duyệt qua từng phần tử i trong mảng array
    for i in array:
        # duyệt qua từng phần tử j trong mảng array.
        for j in array:
            # in ra cặp giá trị (i, j) dưới dạng chuỗi.
            print(str(i)+","+str(j))
# hàm printPairs được gọi với đối số là một mảng [1, 2, 3, 4]
printPairs([1,2,3,4])           