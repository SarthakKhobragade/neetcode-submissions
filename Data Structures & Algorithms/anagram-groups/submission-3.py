class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapp = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            word = strs[i]
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            mapp[tuple(count)].append(word)
        
        for k,v in mapp.items():
            result.append(v)
        

        return result
