def DuongDi(dt, v1, v2):
    # Hàm đệ quy để tìm kiếm đường đi từ v1 đến v2
    def DFS(dt, v1, v2, visited):
        # Đánh dấu đỉnh v1 là đã thăm
        visited[v1] = True

        # Nếu đỉnh v2 được kết nối với v1, trả về True
        if v2 in dt[v1]:
            return True

        # Duyệt qua tất cả các đỉnh kề với v1
        for neighbor in dt[v1]:
            # Nếu đỉnh kề chưa được thăm, tiến hành duyệt đệ quy từ đỉnh kề
            if not visited[neighbor]:
                if DFS(dt, neighbor, v2, visited):
                    return True

        # Nếu không tìm thấy đường đi từ v1 đến v2, trả về False
        return False

    # Khởi tạo danh sách đánh dấu các đỉnh đã thăm
    visited = {v: False for v in dt}

    # Gọi hàm đệ quy DFS để kiểm tra đường đi từ v1 đến v2
    return DFS(dt, v1, v2, visited)

# Ví dụ sử dụng:
dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A']
}
v1 = 'A'
v2 = 'D'
print(DuongDi(dt, v1, v2))  # Kết quả: True, có đường đi từ A đến D trong đồ thị dt
