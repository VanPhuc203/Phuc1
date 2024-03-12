# Insertion at the Beginning of a Singly Linked List
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length +=1

  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
    elif index >= self.length:
      self.append(value)
    else:
      new_node = Node(value)
      current_node = self.head
      for i in range(index-1):
        current_node = current_node.next
      new_node.next = current_node.next
      current_node.next = new_node
      self.length +=1

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length +=1

  def traverse(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(25)
new_linked_list.insert(2, 30)
new_linked_list.traverse()