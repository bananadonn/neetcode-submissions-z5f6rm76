class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        CtoP = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            CtoP[c].append(p)
        
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if CtoP[c] == []:
                return True
            visited.add(c)

            for nbr in CtoP[c]:
                if not dfs(nbr):
                    return False
            visited.remove(c)
            CtoP[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                