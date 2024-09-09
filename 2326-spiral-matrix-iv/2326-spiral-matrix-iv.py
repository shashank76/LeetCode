# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1]*n for _ in range(m)]
        row, col = 0, -1
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        while head is not None:
            r = row + direction[idx][0]
            c = col + direction[idx][1]
            if not (0 <= r < m and 0 <= c < n and grid[r][c] == -1):
                idx = (idx + 1) % 4
                r = row + direction[idx][0]
                c = col + direction[idx][1]
            
            grid[r][c] = head.val
            head = head.next
            row, col = r, c        
        return grid
        