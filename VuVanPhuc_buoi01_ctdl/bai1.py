# Khai báo tên hàm có tên là 'openRussianDoll' nhận vào tham số 'doll'
def openRussianDoll(doll):
    # Kiểm tra nếu số lượng nước búp bê (doll) bằng 1
    if doll == 1:
        # Nếu điều kiện if trên là đúng (số lượng nước búp bê là 1), thì hiển thị thông điệp "All dolls are opened"
        print("All dolls are opened")
        # Nếu điều kiện if là sai, tức là số lượng nước búp bê (doll) không phải là 1, thì chương trình chuyển sang phần else.
    else:
        openRussianDoll(doll-1)
        # Trong phần else, hàm openRussianDoll được gọi lại với tham số doll-1. Quá trình này lặp lại cho đến khi số lượng nước búp bê bằng 1, khi đó thông điệp "All dolls are opened" sẽ được hiển thị
        print("All doll are closed")
# Nhập dữ liệu từ người dùng với hàm input.
doll = int(input())
openRussianDoll(doll)
