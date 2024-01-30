
def merge_dicts(dict1,dict2):
    # Tạo một bản sao của dict1 và lưu vào biến merged. Điều này giúp tránh việc thay đổi dict1 gốc.
    merged = dict1.copy()
    # Duyệt qua từng cặp khóa-giá trị trong dict2.
    for key, value in dict2.items():
        #Nếu khóa hiện tại đã tồn tại trong merged (tức là nó cũng tồn tại trong dict1), thì cộng giá trị của khóa đó trong dict2 vào giá trị hiện tại của khóa đó trong merged.
        if key in merged:
            merged[key] += value
        # Nếu khóa hiện tại không tồn tại trong merged (tức là nó chỉ tồn tại trong dict2), thì thêm khóa đó và giá trị tương ứng vào merged
        else:
            merged[key] = value
    # Trả về từ điển merged sau khi đã hợp nhất và cộng các giá trị của các khóa chung.
    return merged

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':3,'c':4,'d':5}
print(merge_dicts(dict1, dict2))