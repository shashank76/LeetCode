class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0]) 
        farmland_groups = []
        queue = deque()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    queue.append((row, col))
                    land[row][col] = 0
                    farmland_coords = [row, col, -1, -1]
                    max_row, max_col = row, col
                    while queue:
                        r1, c1 = queue.popleft()
                        max_row, max_col = max(max_row, r1), max(max_col, c1)
                        for dr, dc in directions:
                            r2, c2 = r1 + dr, c1 + dc
                            if 0 <= r2 < rows and 0 <= c2 < cols and land[r2][c2] == 1:
                                land[r2][c2] = 0
                                queue.append((r2, c2))
                    farmland_coords[2], farmland_coords[3] = max_row, max_col
                    farmland_groups.append(farmland_coords)
        return farmland_groups
        