class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
        
    def find(self, i):
        p = self.parent[i]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.count-=1
        return 1
    
    def isConnected(self):
        return self.count <= 1

    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        count = 0
        
        for t, i, j in edges:
            if t == 3:
                count+= (alice.union(i, j) | bob.union(i, j))
        
        for t, i, j in edges:
            if t==1:
                count+= alice.union(i, j)
            elif t==2:
                count+= bob.union(i, j)
        
        if alice.isConnected() and bob.isConnected():
            return len(edges) - count
        
        return -1
        