# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            example:
            head = [1,2,3,4], n = 2

            create dummy node
            d = 0,1,2,3,4
            set fast = dummy
            advance fast n + 1

            f = 3
            set slow = d, advance fast and slow until fast is None

            slow = 2

            slow is now at the node right behind the node we want to remove
            set slow.next = slow.next.next
        """

        if not head or n < 1:
            return None

        dummy = ListNode(0, head)
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


        
        