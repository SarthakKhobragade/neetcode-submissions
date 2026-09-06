class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * num_courses

        for course, pre_req in prerequisites:
            adj[pre_req].append(course)
            in_degree[course] += 1
        
        queue = deque([])
        for i, course in enumerate(in_degree):
            if course == 0:
                queue.append(i)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == num_courses else []



