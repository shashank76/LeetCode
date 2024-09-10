# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insertnode(node1, node2, val):
            node1.next = ListNode(val,node2)
        
        def gcd(val1, val2):
            while val2 != 0:
                (val1, val2) = (val2, val1 % val2)
            return val1

        node1, node2 = head, head.next
        while node2:
            insertnode(node1, node2, gcd(node1.val, node2.val))
            node1 = node2
            node2=node2.next

        return head
        