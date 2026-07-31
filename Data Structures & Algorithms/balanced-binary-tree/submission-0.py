# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def traverse(node):
            if not node:
                return 0

            left = 1 + traverse(node.left)
            right = 1 + traverse(node.right)
            if abs(left-right) > 1:
                result[0] = False

            return max(left,right)
        
        traverse(root)

        return result[0]