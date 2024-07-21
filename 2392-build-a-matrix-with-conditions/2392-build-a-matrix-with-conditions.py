class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(cond):
            dictVal = defaultdict(list)
            board = [0] * (k + 1)
            for a, b in cond:
                dictVal[a].append(b)
                board[b] += 1
            q = deque([i for i, v in enumerate(board[1:], 1) if v == 0])
            curr = []
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    curr.append(i)
                    for j in dictVal[i]:
                        board[j] -= 1
                        if board[j] == 0:
                            q.append(j)
            
            if len(curr) == k:
                return curr

        row = dfs(rowConditions)
        col = dfs(colConditions)
        
        if row is None or col is None:
            return []
        
        out = [[0] * k for _ in range(k)]
        matx = [0] * (k + 1)
        
        for i, v in enumerate(col):
            matx[v] = i
        
        for i, v in enumerate(row):
            out[i][matx[v]] = v
        
        return out
        