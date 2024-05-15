class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def BSTTuanTu(self):
        return self._check_BST(self.root)

    def _check_BST(self, node):
        if node is None:
            return True

        if node.left and node.right:
            return False

        return self._check_BST(node.left) and self._check_BST(node.right)


# Create an example binary tree
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


print(tree.BSTTuanTu())  # Output: True