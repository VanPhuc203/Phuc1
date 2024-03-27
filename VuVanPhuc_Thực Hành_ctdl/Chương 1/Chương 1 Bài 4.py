
def pascal_triangle(n):
    result = []  
    for i in range(n + 1):
        row = [1]  
        if result:  
            last_row = result[-1]  
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  
        result.append(row)  
    return result

def print_pascal_triangle(triangle):
    width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        print(" ".join(map(str, row)).center(width))

n = 4  
pascal = pascal_triangle(n)
print_pascal_triangle(pascal)