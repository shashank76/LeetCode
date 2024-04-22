class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        def children(lock):
            out = []
            for i in range(4):
                x = str((int(lock[i]) + 1) % 10)
                out.append(lock[:i] + x + lock[i+1:])
                x = str((int(lock[i]) - 1 + 10) % 10)
                out.append(lock[:i] + x + lock[i+1:])
            return out
            
        visited = set(deadends)
        q = deque()
        q.append(['0000', 0])
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for c in children(lock):
                if c not in visited:
                    visited.add(c)
                    q.append([c, turns+1])
        return -1
        