class Solution:
    def foreignDictionary(self, words: List[str]) -> str:    
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        # 2. Build edges and increment indegrees directly
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(res) if len(res) == len(adj) else ""
