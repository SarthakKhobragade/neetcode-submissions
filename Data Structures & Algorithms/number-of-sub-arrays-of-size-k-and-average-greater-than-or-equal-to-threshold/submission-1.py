class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = 0
        res = 0
        for right in range(len(arr)):
            curr += arr[right]
            if right >= k - 1:
                if curr/k >= threshold:
                    res += 1
                curr -= arr[right - k + 1]
        return res