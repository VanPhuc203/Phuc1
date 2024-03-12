
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def find_second_middle_node(head):
    slow = fast = head
    prev_slow = None

    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    if prev_slow:
        return prev_slow.next
    else:
        return None

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

result = find_second_middle_node(head)
if result:
    print(result.value) 
else:
    print("No second middle node")
