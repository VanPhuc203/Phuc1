def powersOf2(n):
    # Nếu n nhỏ hơn 1, hàm trả về 0, bởi vì không có bội số của 2 nếu n là một số không dương.
    if n < 1:
        return 0
    # Nếu n bằng 1, hàm in ra giá trị 1 và trả về 1
    elif n == 1:
        print(1)
        return 1
    else:
        # Nếu n lớn hơn 1, hàm sử dụng đệ quy để tính giá trị prev, bằng cách gọi lại chính nó với đối số là int(n/2)
        prev = powersOf2(int(n/2))
        # hàm tính giá trị curr bằng cách nhân prev với 2. Sau đó, in ra giá trị curr.
        curr = prev*2
        print(curr)
        # Hàm trả về giá trị của curr, là bội số của 2 cho giá trị n.
        return curr
# hàm powersOf2 được gọi với đối số 6 để in ra các bội số của 2 từ 2^0 đến 2^6.
print (powersOf2(6))