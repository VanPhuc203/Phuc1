class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return self.SoNut(node.left) + 1 + self.SoNut(node.right)

# Tạo các đối tượng Node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Xây dựng cây nhị phân
tree = Binary_Tree()
tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Đếm số nút trong cây
num_nodes = tree.SoNut(tree.root)
print("Số nút trong cây:", num_nodes)
