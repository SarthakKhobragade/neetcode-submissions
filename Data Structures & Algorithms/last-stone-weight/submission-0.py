class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -weight)

        while len(heap) > 1:
            weight1 = -heapq.heappop(heap)
            weight2 = -heapq.heappop(heap)
            diff = abs(weight1-weight2)
            if diff == 0:
                continue
            else:
                heapq.heappush(heap, -diff)
  
        return -heap[0] if heap else 0