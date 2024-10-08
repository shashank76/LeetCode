# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nums = set(nums)
        prev = dummy
        while head is not None:
            if head.val in nums:
                prev.next = head.next
            else:
                prev = head
            head = head.next


        return dummy.next
        