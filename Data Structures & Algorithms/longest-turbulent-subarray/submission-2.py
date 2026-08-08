class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        if len(arr) <= 1:
            return res

        l = 0
        r = 1
        prev = ""

        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r - 1
                prev = ""
        
        return res
