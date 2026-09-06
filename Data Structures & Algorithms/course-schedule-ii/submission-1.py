class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for course, needs_course in prerequisites:
            adj[course].add(needs_course)

        current_path = set()
        completed = []

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
            completed.append(course)
            return True

        for course in range(num_courses):
            if not can_complete(course):
                return []

        return completed