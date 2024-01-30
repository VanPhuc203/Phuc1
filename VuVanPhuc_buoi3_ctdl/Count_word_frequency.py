
def count_word_frequency(words):
    # Khởi tạo một từ điển trống frequency để lưu trữ các từ 
    frequency = {}
    # Duyệt qua từng từ trong danh sách words.
    for word in words:
        # Nếu từ hiện tại đã tồn tại trong từ điển frequency, tăng giá trị của nó lên 1.
        if word in frequency:
            frequency[word] +=1
        #Nếu từ hiện tại chưa tồn tại trong từ điển frequency, thêm nó vào từ điển với giá trị là 1.
        else:
            frequency[word] = 1
    # Trả về từ điển frequency sau khi đã đếm xong tất cả các từ
    return frequency
words = ['apple','orange', 'banana','apple','orange', 'apple']
print( count_word_frequency(words))