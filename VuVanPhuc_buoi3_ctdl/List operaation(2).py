# Khởi tạo hai biến total và count với giá trị ban đầu là 0. total sẽ được sử dụng để tính tổng các số được nhập, và count sẽ đếm số lượng các số được nhập.
total = 0
count = 0
# Bắt đầu một vòng lặp vô hạn. Vòng lặp này sẽ tiếp tục cho đến khi gặp lệnh break
while(True):
    # Yêu cầu người dùng nhập một số. Giá trị này được lưu trong biến inp.
    inp = input('Enter the number:')
    # Nếu người dùng nhập từ ‘done’, thì vòng lặp sẽ kết thúc.
    if inp == 'done': break
    # Chuyển đổi giá trị nhập từ người dùng thành số thực và lưu vào biến value.
    value = float(inp)
    # Cộng giá trị vừa nhập vào tổng total và tăng count lên 1.
    total=total + value
    count = count + 1
    Average = total / count
# Sau khi vòng lặp kết thúc, in ra trung bình. 
print('average:', Average)
