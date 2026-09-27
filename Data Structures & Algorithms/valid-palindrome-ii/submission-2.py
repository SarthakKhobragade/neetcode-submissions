class Solution:
    def validPalindrome(self, s: str) -> bool:
        memo = {}
        def find(i: int, j: int, deleted: bool) -> bool:
            if i >= j:
                return True

            state = (i, j, deleted)
            if state in memo:
                return memo[state]

            if s[i] == s[j]:
                memo[state] = find(i + 1, j - 1, deleted)
            else:
                if deleted:
                    memo[state] = False
                else:
                    memo[state] = find(i + 1, j, True) or find(i, j - 1, True)

            return memo[state]

        return find(0, len(s) - 1, False)
