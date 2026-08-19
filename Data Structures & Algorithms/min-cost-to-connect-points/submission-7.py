class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_vertices = len(points)
        # Step 1: Initialize tracking arrays
        key = [sys.maxsize] * num_vertices
        parent = [-1] * num_vertices
        mst_set = [False] * num_vertices

        # Start with the first vertex
        key[0] = 0 

        # Loop to add all vertices to the MST
        for _ in range(num_vertices):
            
            # Step 2: Linearly search for the minimum key vertex not yet in MST
            min_val = sys.maxsize
            u = -1
            for v in range(num_vertices):
                if not mst_set[v] and key[v] < min_val:
                    min_val = key[v]
                    u = v

            # Step 3: Include the picked vertex in the MST set
            mst_set[u] = True

            # Step 4: Update key values and parent index of adjacent vertices
            for v in range(num_vertices):
                if not mst_set[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < key[v]:
                        key[v] = dist
                        parent[v] = u
        return sum(key)