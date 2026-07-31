class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for c in s:
            if stack and c in mapp:
                if mapp[c] != stack[-1]:
                    return False
                stack.pop()
                continue
            stack.append(c)

        return len(stack) == 0
