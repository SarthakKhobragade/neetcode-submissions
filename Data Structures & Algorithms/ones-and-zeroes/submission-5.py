class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        # Pre-calculate to avoid O(Length of String) inside the recursion
        counts = [(s.count("0"), s.count("1")) for s in strs]

        def find(i, zero, one):
            if i == len(strs):
                return 0

            if (i, zero, one) in memo:
                return memo[(i, zero, one)]

            res = find(i + 1, zero, one)
            z, o = counts[i]    
            if zero >= z and one >= o:
                res = max(res, 1 + find(i + 1, zero - z, one - o))

            memo[(i, zero, one)] = res
            return memo[(i, zero, one)]

        return find(0, m, n)