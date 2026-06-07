# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        g = res
            
        while True:
            mi = -1
            for i in range(len(lists)):
                if lists[i] and (mi == -1 or lists[i].val < lists[mi].val):                                                                                                                                                                                 
                    mi = i
            if mi == -1:
                break
            res.next = ListNode(lists[mi].val)
            res = res.next
            lists[mi] = lists[mi].next                                                                                                                                                                                                                      

        return g.next

