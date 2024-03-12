
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

linked_list = LinkedList(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()
