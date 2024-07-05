# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minima, maxima = float('inf'), -1
        prev, cur, nxt = head, head.next, head.next.next
        crit1, crit2 = 0, 0
        i = 1
        while nxt:
            if (prev.val < cur.val > nxt.val) or (prev.val > cur.val < nxt.val):
                if crit1:
                    maxima = i - crit1
                    minima = min(minima, i - crit2)
                else:
                    crit1 = i
                crit2 = i
            prev, cur, nxt = cur, nxt, nxt.next
            i+=1
                
        return [minima, maxima] if minima != float('inf') else [-1, -1]
        