class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for pre_req in prerequisites:
            course, needs_course = pre_req
            adj[course].add(needs_course)
        
        visited = set()
        memo = {}
        def dfs(course):
            if course in visited:
                return False
            if course in memo:
                return memo[course]
            if not adj[course]:
                return True
    
            visited.add(course)
            for neighbour in adj[course]:
                if not dfs(neighbour):
                    memo[course] = False
                    return False
            visited.remove(course)
            memo[course] = True
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
