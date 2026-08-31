class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def find(i, j, k):
            if k == len(s3):
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            memo[(i,j,k)] = False
            if i < len(s1) and s1[i] == s3[k]:
                memo[(i,j,k)] = find(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                memo[(i,j,k)] = find(i, j + 1, k + 1)
            return memo[(i,j,k)]

        return find(0, 0, 0)
