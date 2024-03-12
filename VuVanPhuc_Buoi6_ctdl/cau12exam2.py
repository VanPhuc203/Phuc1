
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    def reverse_linked_list(node):
        prev = None
        current = node

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def get_middle(node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def compare_lists(list1, list2):
        while list1 and list2:
            if list1.value != list2.value:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    if not head or not head.next:
        return True

    middle_node = get_middle(head)
    second_half_reversed = reverse_linked_list(middle_node)

    return compare_lists(head, second_half_reversed)

head = ListNode(1, ListNode(2))

result = is_palindrome(head)
print(result) 