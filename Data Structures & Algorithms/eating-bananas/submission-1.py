class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def check_valid(num):
            time = 0
            for bananas in piles:
                time += math.ceil(bananas/num)
            
            return time <= h

        while left <= right:
            mid = (left+right)//2
            if check_valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        ## 3 4 5
        return left