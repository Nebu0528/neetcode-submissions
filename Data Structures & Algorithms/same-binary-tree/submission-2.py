# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # do not return True on the first instance so we should check for the following

        #we will check based on if we can traverse the tree properly
        if not p and not q:
            return True

        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        