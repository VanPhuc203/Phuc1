
# how to create a Tuple?
newTuple =  ('a','b','c','d','e')
newTuple1 = tuple('abcde')
print(newTuple1)


# how to access Tuple element? 
newTuple = ('a', 'b','c','d','e')

print(newTuple[1])

print(newTuple1[-1])

print(newTuple1[-2])
# [1:3]: nó sẽ lấy từ phần tử thứ nhất đến phần tử thứ 2 (bỏ phần tử thứ 3)
print(newTuple1[1:3])

# [:3]: lấy từ phần tử đầu đến phần tử thứ 2
print(newTuple1[:3])

# [1:]: lấy phần tử thứ nhất đến hết 
print(newTuple1[1:])