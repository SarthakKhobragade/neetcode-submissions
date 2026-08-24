class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]

        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]


        def union(start, end):
            parent_start = find(start)
            parent_end = find(end)

            if parent_start == parent_end:
                return True
            
            parent[parent_end] = parent_start
            return False 

        for n1,n2 in edges:
            union(n1,n2)
        
        unique_parts = set(find(i) for i in range(n))

        return len(unique_parts)