class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for count, num in heap:
            res.append(num)

        return res