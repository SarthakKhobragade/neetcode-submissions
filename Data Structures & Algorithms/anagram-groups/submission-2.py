class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        size = len(strs)
        seen = [False] * size

        for i in range(size):
            if seen[i]:
                continue
            word = strs[i]
            curr = [word]
            seen[i] = True
            sorted_word = sorted(word)
            for j in range(i+1, size):
                if not seen[j] and sorted_word == sorted(strs[j]):
                    curr.append(strs[j])
                    seen[j] = True
            result.append(curr)
    
        return result