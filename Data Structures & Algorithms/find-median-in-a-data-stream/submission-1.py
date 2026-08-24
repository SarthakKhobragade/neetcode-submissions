class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    def balance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)
        elif len(self.min_heap) > len(self.max_heap):
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.balance()
        
    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 1:
            return float(-self.max_heap[0])
        return (self.min_heap[0] - self.max_heap[0]) / 2.0