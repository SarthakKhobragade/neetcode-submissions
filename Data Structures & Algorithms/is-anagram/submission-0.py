class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for letter in s:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1

        for letter in t:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] -= 1
        
        for k,v in seen.items():
            if v != 0:
                return False

        return True