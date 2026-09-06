class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for pre_req in prerequisites:
            course, needs_course = pre_req
            adj[course].add(needs_course)

        possible = {}
        def can_complete(course, visited):
            if course in possible:
                return possible[course]
            if course in visited:
                return False

            visited.add(course)
            for pre_req in adj[course]:
                if not can_complete(pre_req, visited):
                    return False
            visited.remove(course)
            possible[course] = True
            return possible[course]



        for course in range(numCourses):
            if not can_complete(course, set()):
                return False

        return True
