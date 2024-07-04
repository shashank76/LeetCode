# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            node.val = node.val + node.next.val
            if node.next.val == 0 and node.next.next:
                node = node.next
            else:
                node.next = node.next.next
        return head
        