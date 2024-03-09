class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time_map = {}

        for s, d, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][s].append(d)
            time_map[t][d].append(s)
        
        def dfs(s, adj):
            if s in visited:
                return
            visited.add(s)
            secrets.add(s)
            for val in adj[s]:
                dfs(val, adj)

        for t in sorted(time_map.keys()):
            visited = set()
            for s in time_map[t]:
                if s in secrets:
                    dfs(s, time_map[t])
        return list(secrets)
        