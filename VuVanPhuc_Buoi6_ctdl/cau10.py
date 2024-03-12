
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList():

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


def remove_all(head, val):
  while head and head.value == val:
    head = head.next

  curr = head
  while curr and curr.next:
    if curr.next.value == val:
      curr.next = curr.next.next
    else:
      curr = curr.next
  return head


new_linked_list = LinkedList(1)
new_linked_list.append(2)
new_linked_list.append(6)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)
new_linked_list.append(6)

new_head = remove_all(new_linked_list.head, 6)

values = []
while new_head:
  values.append(str(new_head.value))
  new_head = new_head.next
print("->".join(values))
