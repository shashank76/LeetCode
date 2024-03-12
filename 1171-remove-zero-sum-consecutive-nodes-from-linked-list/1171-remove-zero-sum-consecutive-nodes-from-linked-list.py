# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, head)
        current_node = node
        vals = 0
        vals_to_node = {}
        while current_node:
            vals += current_node.val
            if vals in vals_to_node:
                prev = vals_to_node[vals]
                current_node = prev.next
                p = vals + current_node.val
                while p != vals:
                    del vals_to_node[p]
                    current_node = current_node.next
                    p += current_node.val
                prev.next = current_node.next
            else:
                vals_to_node[vals] = current_node
            current_node = current_node.next

        return node.next
        