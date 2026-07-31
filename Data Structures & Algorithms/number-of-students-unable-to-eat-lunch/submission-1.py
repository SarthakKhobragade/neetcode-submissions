class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        idx = 0

        res = n
        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and students[idx] != sandwich:
                idx += 1
                idx %= n
                cnt += 1

            if students[idx] == sandwich:
                students[idx] = -1
                res -= 1
            else:
                break
        return res