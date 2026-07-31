class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            heapq.heappush(heap, ((x*x+y*y),x,y))
        
        result = []
        count = k
        while count:
            count -= 1
            dist, x,y = heapq.heappop(heap)
            result.append([x,y])
        
        return result

        