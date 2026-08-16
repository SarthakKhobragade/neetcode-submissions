# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        res = 0

        for i in range(len(values)):
            res = max(res, values[i] + values[len(values)-i-1])
        
        return res