class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for k,v in count.items():
            freq[v].append(k)

        result = []

        for i in range(len(freq)-1,-1,-1):
            for item in freq[i]:
                result.append(item)
                if len(result) == target:
                    return result