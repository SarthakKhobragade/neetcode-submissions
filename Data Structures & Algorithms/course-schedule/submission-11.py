class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for course, needs_course in prerequisites:
            adj[course].add(needs_course)

        current_path = set()
        completed = set()

        def can_complete(course):
            if course in current_path:
                return False
            
            if course in completed:
                return True

            current_path.add(course)
            for pre_req in adj[course]:
                if not can_complete(pre_req):
                    return False

            current_path.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not can_complete(course):
                return False

        return True