# Middle of a Singly Linked List
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
  def get(self, index):
        current = self.head
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for __ in range(index):
            current = current.next
        return current
  def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result 
def cau6(linklist):
  if (linklist.length==0): return
  if (linklist.length==1): return linklist.head
  if (linklist.length % 2==0): return linklist.get(int(linklist.length/2)).value
  else: return linklist.get((linklist.length//2)).value

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
print(cau6(new_linked_list))