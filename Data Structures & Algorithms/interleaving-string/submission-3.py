class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        k = len(s3) - 1

        i,j = len(s1)-1,len(s2)-1
        if len(s3) != len(s1) + len(s2):
            return False

        while k >= 0:
            if i >=0 and s1[i] == s3[k]:
                i -= 1
                k -= 1
                continue
            if j >= 0 and s2[j] == s3[k]:
                j -= 1
                k -= 1
            else:
                return False

        return True