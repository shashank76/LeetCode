# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getBatchList(self, node, size):
        
        while node and size > 0:
            node = node.next
            size -=1
        return node
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy
        
        while True:
            kthVal = self.getBatchList(grpPrev, k)
            if not kthVal:
                break
            nextVal = kthVal.next
            
            prev, nxt = kthVal.next, grpPrev.next
            
            while nxt != nextVal:
                tmp = nxt.next
                nxt.next = prev
                prev = nxt
                nxt = tmp
            tmp = grpPrev.next
            grpPrev.next = kthVal
            grpPrev = tmp
        return dummy.next
            