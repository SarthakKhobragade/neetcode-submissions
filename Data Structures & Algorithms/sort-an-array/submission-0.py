class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        while nums:
            val = heapq.heappop(nums)
            res.append(val)
        
        return res
        