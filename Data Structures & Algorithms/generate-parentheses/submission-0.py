class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        size = n * 2
        res = []

        def find(curr, bal):
            if bal < 0:
                return
    
            if len(curr) == size:
                if bal == 0:
                    res.append(''.join(curr))
                return
            
            curr.append("(")
            find(curr, bal + 1)
            curr.pop()
            curr.append(")")
            find(curr, bal - 1)
            curr.pop()
        

        find([], 0)

        return res