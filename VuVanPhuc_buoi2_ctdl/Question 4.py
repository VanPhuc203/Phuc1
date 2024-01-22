def printUnorderedPairs(arrayA, arrayB):
    # duyệt qua từng phần tử i trong mảng arrayA.
    for i in range(len(arrayA)):
        # lồng bên trong vòng lặp đầu tiên, duyệt qua từng phần tử j trong mảng arrayB.
        for j in range(len(arrayB)):
            #kiểm tra xem arrayA[i] có nhỏ hơn arrayB[j] không. Nếu có, in ra cặp giá trị (arrayA[i], arrayB[j]).
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))
printUnorderedPairs([1,2,3,4],[5,6,7,8])