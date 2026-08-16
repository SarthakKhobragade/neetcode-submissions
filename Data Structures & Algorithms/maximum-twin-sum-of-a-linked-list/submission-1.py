# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        curr = head


        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        while curr != slow:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        res = 0 
        while slow:
            res = max(prev.val + slow.val, res)
            prev = prev.next 
            slow = slow.next
    
        return res