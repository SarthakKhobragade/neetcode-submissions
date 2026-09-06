class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        indegree = {c: 0 for c in adj.keys()}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_size = min(len(word1), len(word2))

            if len(word2) < len(word1) and word1[:min_size] == word2[:min_size]:
                return ""
            
            for j in range(min_size):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        
        queue = deque([c for c, d in indegree.items() if d == 0])
        res = []
        while queue:
            char = queue.popleft()
            res.append(char)

            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return ''.join(res) if len(res) == len(adj) else ""

        

