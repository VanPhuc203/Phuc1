class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def CanBangHoanToan(self):
        return self._check_balance(self.root)[0]

    def _check_balance(self, node):
        if node is None:
            return True, 0  # Cây null được cân bằng và có chiều cao 0

        left_balanced, left_height = self._check_balance(node.left)
        if not left_balanced:
            return False, 0  # Nếu cây con trái không cân bằng thì không cần kiểm tra cây con phải

        right_balanced, right_height = self._check_balance(node.right)
        if not right_balanced:
            return False, 0  # Nếu cây con bên phải không cân bằng thì không cần kiểm tra thêm

        # Cây được cân bằng nếu chênh lệch độ cao giữa bên trái và bên phải tối đa là 1
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1



# Tạo một cây nhị phân mẫu.
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /
# 6
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)


print(tree.CanBangHoanToan())  # Output: True