class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = [-1] * len(arr)
        maxx = -1
        for i in range(len(arr)-1,-1,-1):
            curr[i] = maxx
            maxx = max(maxx, arr[i])
        
        return curr

        