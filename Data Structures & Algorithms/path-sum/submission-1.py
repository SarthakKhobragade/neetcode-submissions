# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def find_sum(node, curr):
            if not node:
                return False
                
            if not node.left and not node.right:
                return curr + node.val == targetSum

            left = find_sum(node.left, curr + node.val)
            right = find_sum(node.right, curr + node.val)

            return left or right

        return find_sum(root, 0)

