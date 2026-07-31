from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        waiting = deque([])
        for choice in students:
            waiting.append(choice)

        rotations = 0
        while sandwiches:
            if rotations >= len(waiting):
                return len(waiting)
            if waiting[0] == sandwiches[0]:
                waiting.popleft()
                sandwiches.pop(0)
                rotations = 0
            else:
                waiting.append(waiting.popleft())
                rotations += 1

        return 0