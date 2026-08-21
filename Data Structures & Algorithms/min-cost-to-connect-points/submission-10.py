import sys
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # num_points = len(points)
        # visited = [False] * num_points
        # mst = [1e9] * num_points

        # mst[0] = 0
        # res = 0
        # for _ in range(num_points):
        #     curr_dist = 1e9
        #     curr = -1
        #     for pt in range(num_points):
        #         if not visited[pt] and (curr == -1 or mst[pt] < curr_dist):
        #             curr_dist = mst[pt]
        #             curr = pt

        #     visited[curr] = True
        #     res += curr_dist

        #     for next_pt in range(num_points):
        #         if not visited[next_pt]:
        #             dist = abs(points[curr][0] - points[next_pt][0]) + abs(points[curr][1] - points[next_pt][1])

        #             if dist < mst[next_pt]:
        #                 mst[next_pt] = dist
            
        
        # return res

        ### Kruskals 

        n = len(points)
        
        # --- DSU SETUP (The exact functions we discussed) ---
        parent = [i for i in range(n)] # Everyone is their own boss initially
        
        def find(x):
            if parent[x] == x:
                return x
            # The Magic Trick: Path Compression
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False # Already connected, skip this bridge!
                
            # Corporate Buyout
            parent[root_x] = root_y
            return True
            

        # --- KRUSKAL'S ALGORITHM ---
        
        # Step 1: List out every possible bridge (cost, point_A, point_B)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                # Manhattan distance formula
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
                
        # Step 2: Sort bridges from cheapest to most expensive
        edges.sort()
        
        # Step 3: Start building
        min_cost = 0
        edges_built = 0
        
        for cost, point_a, point_b in edges:
            # Check our DSU clipboard to see if we should build this bridge
            if union(point_a, point_b):
                min_cost += cost
                edges_built += 1
                
                # As soon as we build N - 1 bridges, we are completely connected!
                if edges_built == n - 1:
                    break
                    
        return min_cost
