class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in visited:
                return [visited[val], i]
            visited[nums[i]] = i