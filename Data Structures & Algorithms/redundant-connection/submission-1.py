class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]

        def find(node):
            if parent[node] == node:
                return node
            
            return find(parent[node])


        def union(start, end):
            parent_start = find(start)
            parent_end = find(end)

            if parent_start == parent_end:
                return True
            
            parent[parent_end] = parent_start
            return False 

        for n1,n2 in edges:
            if union(n1,n2):
                return [n1,n2]