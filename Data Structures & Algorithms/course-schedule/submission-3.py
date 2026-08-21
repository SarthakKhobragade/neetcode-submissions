class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, pre_req in prerequisites:
            adj[course].append(pre_req)

        res = []

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for pre_req in adj[course]:
                if not dfs(pre_req):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True



        for course in range(num_courses):
            if not dfs(course):
                return False
        
        return True