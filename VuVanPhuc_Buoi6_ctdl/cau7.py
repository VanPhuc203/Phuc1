# Remove Duplicates from a Singly Linked List
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

    def remove_duplicates(self):
        if not self.head:
            return

        current_node = self.head

        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Example Usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)

print("Original singly linked list:")
linked_list.display()

linked_list.remove_duplicates()

print("Linked list after removing duplicates:")
linked_list.display()
