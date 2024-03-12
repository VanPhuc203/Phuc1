
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head

def display_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

print("Original Sorted Linked List:")
display_linked_list(head)

head = remove_duplicates(head)

print("Sorted Linked List After Removing Duplicates:")
display_linked_list(head)
