def reverse(array):
    #Duyệt qua nửa đầu của mảng (đến giữa mảng) vì khi đảo ngược, phần tử ở vị trí i sẽ được đổi chỗ với phần tử ở vị trí len(array) 
    for i in range(0, int(len(array)/2)):
        #Các phần tử tại vị trí i và other được đổi chỗ giá trị.
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    #In Mảng Sau Khi Đảo Ngược
    print(array)
reverse([2,5,6])