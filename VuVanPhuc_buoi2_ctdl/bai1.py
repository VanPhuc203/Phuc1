# Tạo một mảng
my_array = [1, 2, 3, 4, 5]

# Duyệt qua mảng và in ra từng phần tử
print("Duyệt qua mảng và in ra từng phần tử:")
for element in my_array:
    print(element)

# Duyệt qua mảng và in ra từng phần tử cùng với chỉ số của nó
print("Duyệt qua mảng và in ra từng phần tử cùng với chỉ số:")
for index, element in enumerate(my_array):
    print(f"Index {index}: {element}")

# Duyệt qua mảng theo chỉ số và in ra từng phần tử
print("Duyệt qua mảng theo chỉ số và in ra từng phần tử:")
for i in range(len(my_array)):
    print(my_array[i])
