# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            head = [1,2,3,4], n = 2

            approach

            initiate a dummy node 0 -> 1
            move a fast pointer n + 1 steps ahead
            f = 3
            slow starts and dummy and move both fast and slow until fast is None
            s,f
            0,3
            1,4
            2,None

            slow is directly behind the node we want to remove
            slow.next = slow.next.next - remove the nth node

            O(n) time complexity, O(1) space complexity

            the dummy node helps us in the cases where the node we 
            want to remove is the head node

            head = [1,2], n = 2
            d = 0, 1, 2
            f=d, move head n + 1= 3 steps
            f = none
            slow = d
            s,f
            0,None
            f is already at none, so slow remains at dummy head

            slow.next = slow.next.next
            0.next = 2
            return dummy.next - real head
        """

        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
        

        
        