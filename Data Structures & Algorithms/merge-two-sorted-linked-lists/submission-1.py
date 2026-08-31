# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
            d | l1 | l2
            0 | 1 | 1
                dummy.next = l1, l1 = l1.next, curr = dummy.next
        """

        dummy = ListNode(0)
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return dummy.next

