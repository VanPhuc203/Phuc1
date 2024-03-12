# Merge Two Sorted Linked List
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def mergeTwoLists(list1, list2):

  dummy = ListNode(0)
  current = dummy

  while list1 and list2:
    if list1.val < list2.val:
      current.next = list1
      list1 = list1.next
    else:
      current.next = list2
      list2 = list2.next
    current = current.next

  current.next = list1 if list1 else list2

  return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = mergeTwoLists(list1, list2)

values = []
while merged_list:
  values.append(str(merged_list.val))
  merged_list = merged_list.next
print("->".join(values))
