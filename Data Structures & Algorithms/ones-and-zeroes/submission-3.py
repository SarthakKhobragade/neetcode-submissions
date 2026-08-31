class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        # Pre-calculate to avoid O(Length of String) inside the recursion
        counts = [(s.count("0"), s.count("1")) for s in strs]

        def find(i, zero, one):
            # 1. Check if we went over capacity
            if zero < 0 or one < 0:
                return -float('inf') # Return -infinity so this path is ignored

            # 2. Base case: out of strings
            if i == len(strs):
                return 0

            if (i, zero, one) in memo:
                return memo[(i, zero, one)]

            z, o = counts[i]
            # Choice: Pick (subtract counts) or Skip
            memo[(i, zero, one)] = max(
                1 + find(i + 1, zero - z, one - o),
                find(i + 1, zero, one),
            )
            return memo[(i, zero, one)]

        return find(0, m, n)