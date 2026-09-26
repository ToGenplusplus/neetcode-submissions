# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
            321 + 654 = 975

            361 + 664 = 1025

            carry = 0
            1 6 3
             4 6 6

            l1 l2 carry , result
            1 4 0 5
            6 6 0 12, carry = 1
            3 6 1 10, carry = 1


             if l1 or l2 is none, default to 0
             add l1 + l2 + carry
             store result % 10 in node
             set carry to result // 10
        """

        carry = 0
        dummy = ListNode()
        res = dummy

        while l1 or l2 or carry:
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            result = l1_val + l2_val + carry
            res.next = ListNode(result % 10)
            carry = result // 10

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

            res = res.next

        return dummy.next