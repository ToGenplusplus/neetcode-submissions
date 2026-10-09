# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
            321 + 654 = 975
            1  2 3
            4. 5. 6

            361 + 659 = 1020
            l1, 1 6 3
            l2, 9 5 6
            0 2 0 1

            l1 l2 carry, total (node.val), nxt_carry
            1 9 0, 0, 1
            6 5 1, 2, 1
            3 6 1, 0, 1
            none(0), none(0), 1, 1, 0

            node.val is % 10
            carry is total // 10
        """

        carry = 0
        dummy = ListNode()
        res = dummy

        while l1 or l2 or carry:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry

            val = total % 10
            carry = total // 10

            res.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            res = res.next

        return dummy.next

            
