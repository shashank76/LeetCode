# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reversed_list(node):
            prev, curr = None, node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt

            return prev
        
        vals = reversed_list(head)
        carry = 0
        curr, prev = vals, None

        while curr:
            val = curr.val * 2 + carry
            curr.val = val % 10
            carry = 1 if val > 9 else 0
            prev, curr = curr, curr.next

        if carry:
            prev.next = ListNode(carry)

        return reversed_list(vals)

    
            
            
                