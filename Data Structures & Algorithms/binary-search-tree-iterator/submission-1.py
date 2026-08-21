# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.inorder(root)
        self.ptr = 0

    def next(self) -> int:
        # if self.ptr >= len(self.res):
        #     return None
        val =  self.res[self.ptr]
        self.ptr += 1
        return val
        

    def hasNext(self) -> bool:
        if self.ptr >= len(self.res):
            return False
        return self.res[self.ptr] != None


    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()