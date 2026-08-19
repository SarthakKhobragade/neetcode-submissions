class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                adj[(x1,y1)].append(((x2,y2), abs(x1-x2) + abs(y1-y2)))
                adj[(x2,y2)].append(((x1,y1), abs(x1-x2) + abs(y1-y2)))
        
        start = points[0]
        heap = [(0, (start[0],start[1]))]
        res = 0
        visited = set()
        while heap:
            weight, source_pt = heapq.heappop(heap)
            if source_pt in visited:
                continue
            res += weight
            visited.add(source_pt)
            for pt, wei in adj[source_pt]:
                if pt not in visited:
                    heapq.heappush(heap, (wei, pt))

        return res