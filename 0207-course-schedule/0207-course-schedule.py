class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = defaultdict(list)
        visited = set()
        for course, prereq in prerequisites:
            preReqMap[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            elif  preReqMap[course] == []:
                return True
            visited.add(course)
            for i in preReqMap[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            preReqMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        