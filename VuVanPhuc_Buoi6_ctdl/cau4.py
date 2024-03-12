
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_at_index(self, index):
        if not self.head or index < 0:
            return None

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            return deleted_node

        current_node = self.head
        for _ in range(index - 1):
            if current_node.next is None:
                return None  
            current_node = current_node.next

        if current_node.next is None:
            return None 

        deleted_node = current_node.next
        current_node.next = current_node.next.next
        deleted_node.next = None
        return deleted_node

# Example Usage:
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()

deleted_node = linked_list.delete_at_index(1)
if deleted_node:
    print(f"Deleted Node: {deleted_node.value}")
linked_list.display()
