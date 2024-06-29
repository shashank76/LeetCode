class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors=[[] for _ in range(n)]
        queue=deque()
        answer=[set() for _ in range(n)]
        nodeCount=[0]*n
        
        for edge in edges:
            ancestors[edge[0]].append(edge[1])
            nodeCount[edge[1]]+=1
        
        
        for i in range(len(nodeCount)):
            if nodeCount[i]==0:
                queue.append(i)
        
        while queue:
            cur=queue.pop()
            for i in ancestors[cur]:
                answer[i].add(cur)
                answer[i].update(answer[cur])
                nodeCount[i]-=1
                
                if nodeCount[i] == 0:
                    queue.append(i)
                    
        answer=[(sorted(list(s))) for s in answer]
        return answer 
    
            
        