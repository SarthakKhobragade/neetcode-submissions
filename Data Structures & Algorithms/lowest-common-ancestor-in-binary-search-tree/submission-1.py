# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def find(node):
            if node == p or node == q or not node:
                return node

            left = find(node.left)
            right = find(node.right)

            if not left:
                return right
            elif not right:
                return left
            else:
                return node

        return find(root)
