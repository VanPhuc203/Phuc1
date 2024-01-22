def printUnorderedPairs(arrayA, arrayB):
    #Vòng lặp đầu tiên duyệt qua từng phần tử i trong mảng arrayA.
    for i in range(len(arrayA)):
        #Vòng lặp thứ hai, lồng bên trong vòng lặp đầu tiên, duyệt qua từng phần tử j trong mảng arrayB.
        for j in range(len(arrayB)):
            #Vòng lặp thứ ba, lồng bên trong cả hai vòng lặp trên, duyệt qua từ 0 đến 99999, nhưng không thực hiện bất kỳ công việc cụ thể nào.
            for k in range(0,100000):
                #Trong mỗi lần lặp của vòng lặp thứ ba, hàm sử dụng hàm print để in ra cặp giá trị (arrayA[i], arrayB[j]) dưới dạng chuỗi.
                print(str(arrayA[i]) + "," + str(arrayB[j]))
printUnorderedPairs([1,2,3],[4,5,6])