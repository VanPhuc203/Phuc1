
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if value < temp.value:
                    if not temp.left:
                        temp.left = new_node
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = new_node
                        break
                    temp = temp.right

    def contains(self, target):
        temp = self.root
        while temp:
            if target == temp.value:
                return True
            elif target < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False


bst = BinarySearchTree()
bst.insert(8)
bst.insert(4)
bst.insert(13)
bst.insert(3)
bst.insert(7)

print(bst.contains(8))  
print(bst.contains(5)) 
