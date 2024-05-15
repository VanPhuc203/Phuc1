class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def CayCon(cay1, cay2):
    if cay2:  # Nếu cây con là None, luôn là cây con của cây gốc
        return True
    if not cay1:  # Nếu cây gốc là None nhưng cây con không phải, không thể là cây con
        return False
    # Kiểm tra từng nút của cây gốc
    return (
        (cay1.info == cay2.info) and
        CayCon(cay1.left, cay2.left) and
        CayCon(cay1.right, cay2.right)
    )

# Tạo cây gốc
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tạo cây con từ cây gốc bằng cách cắt một phần của cây gốc
subtree = root.left
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Kiểm tra xem cây con có phải là cây con của cây gốc không
is_subtree = CayCon(root, subtree)
print("Cây con là cây con của cây gốc:", is_subtree)


