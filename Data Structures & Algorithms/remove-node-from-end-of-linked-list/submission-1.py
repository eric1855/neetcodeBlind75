# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        head = ListNode()
        head.next = tmp
        
        front = end = head

        for i in range(n):
            end = end.next

        # none, 1, 2, none
        res = None #1
        while end:
            print("hi")
            res = front
            front = front.next
            end = end.next
        res.next = front.next
        return head.next