# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.reverseListRecursive(head)
        return self.reverseListIterative(head)


    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            examples: head: [0,1,2,3]
            base case
                if head == None or Head.next == None 
                    return Head - this becomes our new head

                3 - return head
                2.next = 3.next = 2 return 3(newhead)
                1.next = 2.next = 1 return 3(newhead)
                1.next = None
        """
        if not head or not head.next:
            return head

        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None

        return new_head

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            examples: head: [0,1,2,3]
            prev= None
            nxt = 0.next = 1
            0.next = prev
            prev = curr
            curr = nxt
            nxt = 1.next = 2
            1.next = prev
        """
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    