class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for num in nums:
            heapq.heappush(self.heap, num)
            self.balance()

    def balance(self):
        while len(self.heap) > self.size:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.balance()
        return self.heap[0]


