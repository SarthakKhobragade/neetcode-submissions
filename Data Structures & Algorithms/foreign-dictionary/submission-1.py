class Solution:
    def foreignDictionary(self, words: List[str]) -> str:    
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid prefix check (e.g., ["abc", "ab"])
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # First differing character defines the directed edge
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        indegree = {c: 0 for c in adj}
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1

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
