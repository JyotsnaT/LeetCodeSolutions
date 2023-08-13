'''
Author : Jyotsna

This function implements solution to  path sum III that requires DFS 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
           return 0

        num_paths = 0
        def pathSumAtNode(root, targetSum):
            nonlocal num_paths

            if root:
                if root.val == targetSum:
                    num_paths += 1

                pathSumAtNode(root.left, targetSum-root.val)
                pathSumAtNode(root.right, targetSum-root.val)
            return 
        
        def pathSumAbs(root, targetSum):
            if not root:
                return
            pathSumAtNode(root, targetSum)
            pathSumAbs(root.left, targetSum)
            pathSumAbs(root.right, targetSum)
        
        pathSumAbs(root, targetSum)
        return num_paths

