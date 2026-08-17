# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
       l1: 1,2,4 l2: 1 3 5 6

        d = 0,l1
        prev = d

        p.next, l1, l2
        1,1,1 l1 <= l2, p.next = l1, l1 = l1.next, prev = prev.next
        1,2,1 l2 < l1, p.next = l2, l2 = l2.next, prev = prev.next
        1,2,3 l1 <= l2, p.next = l1, l1 = l1.next, prev = prev.next
        2,4,3 l2 < l1, p.next = l2, l2 = l2.next, prev = prev.next
        3,4,5 l1 <= l2, p.next = l1, l1 = l1.next, prev = prev.next
        4,None,5 l1 is none, nothing to compare, set p.next to l2
            since l1 and l2 are already sorted and l1 last value is less than l2
            when l1 is done, pointing p.next to l2 guarantees to maintain the sorted order

        we return dummy.next - points to the real head of the sorted merged list

        Time complexity -O(1) each node is visited at most once

        space complexity - O(1)
        """

        dummy = ListNode(0,list1)
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
