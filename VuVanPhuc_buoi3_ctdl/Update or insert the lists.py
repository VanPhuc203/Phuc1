# Đây là danh sách ban đầu mà chúng ta sẽ thao tác.
myList = ['H','E','L','L','O']
# Phương thức pop xóa phần tử tại chỉ số được chỉ định (ở đây là 2) khỏi danh sách và trả về giá trị của nó. Trong trường hợp này, nó sẽ xóa phần tử ‘L’ đầu tiên (vì chỉ số bắt đầu từ 0). Danh sách sau khi thực hiện lệnh này sẽ trở thành ['H', 'E', 'L', 'O'].
myList  .pop(2)
# Lệnh del xóa các phần tử từ chỉ số 1 đến 3 (không bao gồm 3) khỏi danh sách. Trong trường hợp này, nó sẽ xóa các phần tử ‘E’ và ‘L’. Danh sách sau khi thực hiện lệnh này sẽ trở thành ['H', 'O'].
del myList[1:3]
# Phương thức remove xóa phần tử đầu tiên có giá trị bằng ‘H’ khỏi danh sách. Danh sách sau khi thực hiện lệnh này sẽ trở thành ['O'].
myList.remove('H')
# in ra danh sách sau khi đã thực hiện tất cả các thao tác xóa. Kết quả in ra sẽ là ['O'].
print(myList)