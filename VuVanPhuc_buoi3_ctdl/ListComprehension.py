# danh sách ban đầu mà chúng ta sẽ thao tác
#1
prev_List = [-2,-3,-4,5,7,8,9,20,22]
# Đây là một biểu thức list comprehension. Nó duyệt qua từng số trong prev_list. Nếu số đó lớn hơn 0, nó sẽ được thêm vào new_list. Nếu không, số 0 sẽ được thêm vào new_list.
new_List = [number if number >  0 else 0 for number in prev_List]
# Cuối cùng, in ra danh sách new_list. Kết quả in ra sẽ là [0, 0, 0, 5, 7, 8, 9, 20, 22].
print(new_List)




# 2
# Định nghĩa hàm get_number nhận một số làm tham số
def get_number(number):
    # Nếu số đó lớn hơn 0, hàm sẽ trả về chính số đó. Nếu không, hàm sẽ trả về chuỗi ‘negative number’.
    if number > 0:
        return number
    else:
        return 'negative number'
# Đây là danh sách ban đầu mà chúng ta sẽ thao tác. 
prev_List = [-20,-15,-12,-10,-8,-5,5,10,12,13,20]
# 1.	Đây là một biểu thức list comprehension. Nó duyệt qua từng số trong prev_list và áp dụng hàm get_number cho mỗi số, sau đó lưu kết quả vào new_list.
new_List = [get_number(number) for number in  prev_List ]
# in ra danh sách new_list. Kết quả in ra sẽ là ['negative number', 'negative number', 'negative number', 'negative number', 2, 'negative number', 5, 10, 12,13,20].
print(new_List)



# 3
# Đây là danh sách ban đầu mà chúng ta sẽ thao tác.
prev_List =[1,2,3]
# duyệt qua từng phần tử i trong prev_list, nhân i với 2, và lưu kết quả vào new_list.
new_List = [i*2 for i in prev_List]
# In ra danh sách prev_list. Kết quả in ra sẽ là [1, 2, 3].
print(prev_List)
# Cuối cùng, in ra danh sách new_list. Kết quả in ra sẽ là [2, 4, 6].
print(new_List)




#4 Accessing the list

# Đây là danh sách ban đầu mà chúng ta sẽ thao tác.
shoppinglist = ['milk', 'butter', 'cheese','cream']
# Bắt đầu một vòng lặp for, với i là chỉ số của từng phần tử trong shoppingList.
for i in range(len(shoppinglist)):
    # Trong mỗi lần lặp, nó thêm chuỗi ’ +1’ vào cuối phần tử hiện tại trong shoppingList.
    shoppinglist[i] = shoppinglist[i] + '+1'
    # in ra phần tử đã được cập nhật
    print(shoppinglist[i])
