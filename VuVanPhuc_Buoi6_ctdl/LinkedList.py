class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

new_node = Node(10)
print(new_node)

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f"Person {self.name}- {self.age}"

new_persom = Person("Elshad", 20)
# print(new_persom)


class LinkedList:
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result    

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
        new_node = Node(value)
        if index ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            return False
        while current:
            if current.value == target:
                return index 
            current = current.next
            index += 1
        return -1
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
    def set_value(self, index, value):
        temp = self.get(index)
        print(temp)
        if temp:
            temp.value = value
            return True
        return False
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node 
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

        

        
    
        
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.delete_all())
print(new_linked_list)
# print(new_linked_list.pop().value)
# print(new_linked_list.get(-1))
# print(new_linked_list.set_value(2,50))
# print(new_linked_list.search(20))
# new_linked_list.traverse()
# new_linked_list.prepend(40)
# print(new_linked_list)
# new_linked_list.insert(1,50)
# print(new_linked_list)

# new_linked_list= LinkedList()
# print(new_linked_list.head.value)