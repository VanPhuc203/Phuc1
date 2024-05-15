class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def Chep(self):
        return self._chep(self.root)

    def _chep(self, node):
        if node is None:
            return None
        node_new = Node(node.info)
        node_new.left = self._chep(node.left)
        node_new.right = self._chep(node.right)
        return node_new


# Tạo các đối tượng Node cho cây gốc
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Xây dựng cây nhị phân gốc
tree = Cay()
tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Sao chép cây nhị phân gốc
tree_copy = Cay()
tree_copy.root = tree.Chep()

# In các node của cây sao chép để kiểm tra
def in_cay(node):
    if node:
        in_cay(node.left)
        print(node.info, end=" ")
        in_cay(node.right)

print("Cây gốc:")
in_cay(tree.root)
print("\nCây sao chép:")
in_cay(tree_copy.root)
