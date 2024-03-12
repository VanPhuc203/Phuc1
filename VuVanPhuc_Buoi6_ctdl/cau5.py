# Reverse a Singly Linked List
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
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

def reverse_linked_list(head):
  if head is None or head.next is None:
    return head
  prev = None
  curr = head
  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
  return prev

new_linked_list = LinkedList(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)

new_reverse = reverse_linked_list(new_linked_list.head)

values = []
while new_reverse:
  values.append(str(new_reverse.value))
  new_reverse = new_reverse.next
print("->".join(values))