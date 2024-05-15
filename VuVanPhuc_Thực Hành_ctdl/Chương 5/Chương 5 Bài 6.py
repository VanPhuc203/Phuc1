class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.height = 1

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraAVL(self):
        return self._kiemTraAVL(self.root)

    def _kiemTraAVL(self, node):
        if node is None:
            return True
        height_left = self._height(node.left)
        height_right = self._height(node.right)
        if abs(height_left - height_right) <= 1 and self._kiemTraAVL(node.left) is True and self._kiemTraAVL(node.right) is True:
            return True
        return False

    def _height(self, node):
        if node is None:
            return 0
        return node.height


# Tạo các đối tượng Node
node1 = Node(10)
node2 = Node(5)
node3 = Node(15)
node4 = Node(2)
node5 = Node(8)
node6 = Node(12)
node7 = Node(20)

# Xây dựng cây nhị phân
tree = Cay()
tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Kiểm tra xem cây là cây AVL hay không
is_avl = tree.KiemTraAVL()
print("Cây là một cây AVL:", is_avl)
