def Dao(mang):
    rows, cols = len(mang), len(mang[0])
    max_area = 0

    # Tạo mảng lưu chiều cao của các đảo
    heights = [0] * cols

    for row in range(rows):
        for col in range(cols):
            # Nếu ô là đất, tăng chiều cao của đảo
            if mang[row][col] == 1:
                heights[col] += 1
            else:
                # Nếu ô là nước, reset chiều cao của đảo
                heights[col] = 0

        # Tính diện tích lớn nhất của đảo có dạng hình chữ nhật
        stack = []
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area

# Ví dụ sử dụng
mang = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1]
]

print("Diện tích lớn nhất của các đảo:", Dao(mang))
