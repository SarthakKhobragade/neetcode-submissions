class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj = defaultdict(list)
        for i in range(len(edges)):
            source, dest = edges[i]
            weight = succProb[i]
            adj[source].append((dest, weight))
            adj[dest].append((source, weight))


        heap = [(-1.0, start_node)]
        visited = set()
        while heap:
            weight, node = heapq.heappop(heap)
            weight = -weight
            if node == end_node:
                return weight
            if node in visited:
                continue
            
            visited.add(node)
            
            for nei, wei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (-weight*wei, nei))
        
        return 0
