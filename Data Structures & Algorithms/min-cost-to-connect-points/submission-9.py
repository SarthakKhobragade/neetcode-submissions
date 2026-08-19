import sys
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        visited = [False] * num_points
        mst = [1e9] * num_points

        mst[0] = 0
        res = 0
        for _ in range(num_points):
            curr_dist = 1e9
            curr = -1
            for pt in range(num_points):
                if not visited[pt] and (curr == -1 or mst[pt] < curr_dist):
                    curr_dist = mst[pt]
                    curr = pt

            visited[curr] = True
            res += curr_dist

            for next_pt in range(num_points):
                if not visited[next_pt]:
                    dist = abs(points[curr][0] - points[next_pt][0]) + abs(points[curr][1] - points[next_pt][1])

                    if dist < mst[next_pt]:
                        mst[next_pt] = dist
            
        
        return res
