class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        stk = [(temperatures[0], 0)]
        for i in range(1, size):
            while stk and stk[-1][0] < temperatures[i]:
                diff = i - stk[-1][1]
                res[stk[-1][1]] = diff
                stk.pop()
            stk.append((temperatures[i], i))

        return res
