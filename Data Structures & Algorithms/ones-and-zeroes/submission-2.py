class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def find(i, zero, one):
            if zero < 0 or one < 0:
                return -1

            if i == len(strs):
                return 0

            if (i, zero, one) in memo:
                return memo[(i, zero, one)]

            memo[(i, zero, one)] =  max(
                1 + find(i + 1, zero - strs[i].count("0"), one - strs[i].count("1")),
                find(i + 1, zero, one),
            )
            return memo[(i, zero, one)]

        return find(0, m, n)
