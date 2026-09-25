class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        threshold = len(nums) // 3

        for num in nums:
            freq[num] += 1

        res = []
        for num, count in freq.items():
            if count > threshold:
                res.append(num)

        return res