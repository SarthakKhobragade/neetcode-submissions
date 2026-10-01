class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [(temperatures[0], 0)]
        for i in range(1,len(temperatures)):
            while stk and stk[-1][0] < temperatures[i]:
                diff = i - stk[-1][1]
                res[stk[-1][1]] = diff
                stk.pop()
            stk.append((temperatures[i], i))

        return res