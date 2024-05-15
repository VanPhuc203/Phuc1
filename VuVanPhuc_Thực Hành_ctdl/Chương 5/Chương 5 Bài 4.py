class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        if node.left is not None and node.right is not None:
            return 1 + self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)
        elif node.left is not None:
            return self.SoNutTrungGian(node.left)
        elif node.right is not None:
            return self.SoNutTrungGian(node.right)
        else:
            return 0



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
node3.left = node5
node3.right = node6
node6.left = node7

# Đếm số nút trung gian trong cây
num_intermediate_nodes = tree.SoNutTrungGian(tree.root)
print("Số nút trung gian trong cây:", num_intermediate_nodes)
