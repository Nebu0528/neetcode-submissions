# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                return [True,0]
            
            #check for balanced bst by getting distance for left and right subtree

            l = dfs(node.left)
            r = dfs(node.right)

            #this will determine True or False
            balanced = l[0] and r[0] and abs(l[1]-r[1]) <= 1

            #compute the height
            height = max(l[1], r[1])+1

            return [balanced, height]
        
        return dfs(root)[0]





            






            

            
            

            

            
