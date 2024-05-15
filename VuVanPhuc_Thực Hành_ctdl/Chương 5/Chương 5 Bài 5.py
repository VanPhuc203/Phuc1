class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraBST(self):
        return self._kiemTraBST(self.root, float('-inf'), float('inf'))

    def _kiemTraBST(self, node, min, max):
        if node is None:
            return True
        if node.info < min or node.info > max:
            return False
        return (self._kiemTraBST(node.left, min, node.info - 1) and
                self._kiemTraBST(node.right, node.info + 1, max))


# Tạo các đối tượng Node
node1 = Node(4)
node2 = Node(2)
node3 = Node(6)
node4 = Node(1)
node5 = Node(3)
node6 = Node(5)
node7 = Node(7)

# Xây dựng cây nhị phân
tree = Cay()
tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Kiểm tra xem cây là cây BST hay không
is_bst = tree.KiemTraBST()
print("Cây là một cây BST:", is_bst)
