#chương trình yêu cầu người dùng nhập số ngày mà họ muốn tính trung bình nhiệt độ.
numDays = int(input("How many day's temp?:"))
#Biến total được khởi tạo với giá trị 0. Nó sẽ được sử dụng để tính tổng nhiệt độ cao nhất của tất cả các ngày
total = 0
#Vòng lặp này chạy từ 1 đến numDays. Mỗi lần lặp tương ứng với một ngày.
for i in range (1, numDays +1):
     #chương trình yêu cầu người dùng nhập nhiệt độ cao nhất của ngày đó. Giá trị này được lưu trong biến nextDay.
     nextDay = int(input("Day"+ str(i)+"ds hight temp:"))
     #Nhiệt độ cao nhất của ngày đó được cộng vào tổng total.
     total+= nextDay
#chương trình tính trung bình nhiệt độ bằng cách chia tổng total cho số ngày numDays. Kết quả được làm tròn đến hai chữ số thập phân.
avg = round(total / numDays, 2)
#chương trình in ra trung bình nhiệt độ.
print("\nAverage= "+ str(avg))