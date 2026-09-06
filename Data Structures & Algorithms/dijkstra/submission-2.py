class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for source, dest, weight in edges:
            adj[source].append((weight, dest))

        heap = []
        heapq.heappush(heap, (0, src))
        visited = set()
        dist = {x: -1 for x in range(n)}

        while heap:
            weight, node = heapq.heappop(heap)
            visited.add(node)
            if dist[node] == -1:
                dist[node] = weight

            for wei, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (weight + wei, nei))

        return dist
