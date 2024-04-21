class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        if [source, destination] in edges:
            return True

        dictVals = defaultdict(set)
        for edge in edges:
            dictVals[edge[0]].add(edge[1])
            dictVals[edge[1]].add(edge[0])

        listVals = [dictVals[source]]
        visited = [False] * n
        while listVals:
            new_list = []
            for vals in listVals:
                if destination in vals:
                    return True
                for node in vals:
                    if visited[node]:
                        continue
                    visited[node] = True
                    new_list.append(dictVals[node])
            listVals = new_list

        return False
        
        