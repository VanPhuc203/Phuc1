class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def SoSanh(self, cay2):
        return self._SoSanh(self.root, cay2.root)

    def _SoSanh(self, node1, node2):
        # Trường hợp cả hai cây đều rỗng
        if node1 is None and node2 is None:
            return True

        # Trường hợp cả hai cây đều không rỗng
        if node1 is not None and node2 is not None:
            return ((node1.info == node2.info) and
                    self._SoSanh(node1.left, node2.left) and
                    self._SoSanh(node1.right, node2.right))

        # Trường hợp một trong hai cây rỗng
        return False


# Tạo cây nhị phân thứ nhất
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

tree1 = BinaryTree(node1)

# Tạo cây nhị phân thứ hai giống với cây nhị phân thứ nhất
node1_copy = Node(1)
node2_copy = Node(2)
node3_copy = Node(3)
node4_copy = Node(4)
node5_copy = Node(5)

node1_copy.left = node2_copy
node1_copy.right = node3_copy
node2_copy.left = node4_copy
node2_copy.right = node5_copy

tree2 = BinaryTree(node1_copy)

# So sánh hai cây nhị phân
result = tree1.SoSanh(tree2)
print("Hai cây nhị phân giống nhau:", result)
