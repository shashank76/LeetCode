"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = { None: None}
        
        cur = head
        
        while cur:
            val = Node(cur.val)
            copyDict[cur] = val
            cur = cur.next
            
        cur = head
        while cur:
            val = copyDict[cur]
            val.next = copyDict[cur.next]
            val.random = copyDict[cur.random]
            cur = cur.next
        
        return copyDict[head]
            
        