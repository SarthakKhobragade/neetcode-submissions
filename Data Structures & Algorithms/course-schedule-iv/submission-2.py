class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        pre_reqs = {}
        for course, pre_req in prerequisites:
            adj[course].add(pre_req)


        # def build_pre_reqs(node):
        #     if node in pre_reqs:  # memoization
        #         return pre_reqs[node]
            
        #     result = set()
        #     for prereq in adj[node]:
        #         result.add(prereq)
        #         # Add ALL prerequisites of this prerequisite
        #         result.update(build_pre_reqs(prereq))
            
        #     pre_reqs[node] = result
        #     return result

        def build_pre_reqs(node):
            if node not in pre_reqs:
                pre_reqs[node] = set()
                for nei in adj[node]:
                    pre_reqs[node].add(nei)
                    build_pre_reqs(nei)
                    pre_reqs[node].update(pre_reqs[nei])

        for course in range(numCourses):
            build_pre_reqs(course)


        res = []
        for course, pre_req in queries:
            if pre_req not in pre_reqs[course]:
                res.append(False)
            else:
                res.append(True)
    
        return res