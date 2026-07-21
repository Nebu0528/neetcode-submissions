# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root, p, q):
            if root is None or p is None or q is None:
                return None
            
            #move to the left if p,q is less than current node val
            #else if p q have values greater than current node val
            #else return root

            if max(p.val, q.val) < root.val:
                return dfs(root.left, p, q)
            elif min(p.val, q.val) > root.val:
                return dfs(root.right, p,q)
            else:
                return root
            
        
        return dfs(root,p,q)

        
        