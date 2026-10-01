class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for ast in asteroids:
            while stk and ast < 0 and stk[-1] > 0:
                diff = ast + stk[-1]
                if diff < 0:
                    stk.pop()
                elif diff > 0:
                    ast = 0
                    break
                else:
                    ast = 0
                    stk.pop()
            if ast:
                stk.append(ast)

        return stk