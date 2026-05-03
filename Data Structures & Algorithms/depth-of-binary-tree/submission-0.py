# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr):

            if not root:
                return curr
            
            right, left = curr + 1, curr + 1

            if root.right:
                right = dfs(root.right, curr + 1)

            if root.left:
                left = dfs(root.left, curr + 1)

            return max(left, right)


        return dfs(root, 0)


