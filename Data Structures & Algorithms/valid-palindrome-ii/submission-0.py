class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def find(i,j, deleted):
            if i >= j:
                return True

            if s[i] == s[j]:
                return find(i+1,j-1, deleted)
            else:
                if deleted:
                    return False
                return find(i+1,j, True) or find(i, j-1, True)
            
        return find(0,len(s)-1, False)