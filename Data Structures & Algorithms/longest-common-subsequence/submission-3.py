class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        cache = {}
        def lcs(i,j):
            if i >= size1 or j >= size2:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if text1[i] == text2[j]:
                return 1 + lcs(i+1,j+1)
            else:
                 cache[(i,j)] = max(lcs(i,j+1),lcs(i+1,j))
                 return cache[(i,j)]
                
        return lcs(0,0)