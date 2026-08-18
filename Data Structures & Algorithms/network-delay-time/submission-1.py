class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, w in times:
            adj[s].append((d, w))

        visited = set()
        min_heap = [(0, k)]
        result = 0

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            result = max(result, weight)

            for new_node, new_weight in adj[node]:
                if new_node not in visited:
                    heapq.heappush(min_heap, (weight + new_weight, new_node))

        return result if len(visited) == n else -1