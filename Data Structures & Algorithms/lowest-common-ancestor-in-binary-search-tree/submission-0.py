# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def find(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = find(node.left)
            right = find(node.right)

            if left and right:
                return node

            if not left:
                return right
            else:
                return left

        return find(root)
