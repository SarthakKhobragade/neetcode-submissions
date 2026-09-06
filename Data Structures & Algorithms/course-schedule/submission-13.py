class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * num_courses

        for course, pre_req in prerequisites:
            indegree[course] += 1
            adj[pre_req].append(course)
        
        queue = deque([])
        for course in range(num_courses):
            if indegree[course] == 0:
                queue.append(course)

        topo = []
        while queue:
            course = queue.popleft()
            topo.append(course)

            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return len(topo) == num_courses

