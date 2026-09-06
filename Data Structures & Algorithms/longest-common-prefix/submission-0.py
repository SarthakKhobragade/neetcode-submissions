class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_size = int(1e9)
        for word in strs:
            min_size = min(min_size, len(word))

        res = []
        for i in range(min_size):
            char = strs[0][i]
            for word in strs:
                if char != word[i]:
                    return ''.join(res)
            res.append(char)
    
        return ''.join(res)