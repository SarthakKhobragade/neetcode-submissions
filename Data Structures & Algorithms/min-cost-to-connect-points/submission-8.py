import sys
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        
        # The ONLY two trackers we need:
        # 1. Is this point officially part of our network?
        in_network = [False] * num_points
        
        # 2. What is the cheapest bridge we can build to this point?
        # Start everyone at infinity, except point 0.
        min_cost = [sys.maxsize] * num_points
        min_cost[0] = 0 
        
        total_cost = 0
        
        for _ in range(num_points):
            # STEP 1: Scan the array for the cheapest unconnected point
            shortest_bridge = sys.maxsize
            curr = -1
            
            for i in range(num_points):
                if not in_network[i] and min_cost[i] < shortest_bridge:
                    shortest_bridge = min_cost[i]
                    curr = i
                    
            # STEP 2: Officially add it to the network and pay the cost
            in_network[curr] = True
            total_cost += shortest_bridge
            
            # STEP 3: Update the array for the remaining unconnected points
            for next_point in range(num_points):
                if not in_network[next_point]:
                    # Distance from our newly added point to this unconnected point
                    dist = abs(points[curr][0] - points[next_point][0]) + \
                           abs(points[curr][1] - points[next_point][1])
                    
                    # If this new bridge is cheaper than whatever we had before, overwrite it
                    if dist < min_cost[next_point]:
                        min_cost[next_point] = dist
                        
        return total_cost