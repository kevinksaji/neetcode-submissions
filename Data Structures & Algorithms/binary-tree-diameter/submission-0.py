# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0  # tracks global max

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0  # height of empty subtree = 0

            # heights of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # possible diameter passing through this node
            diameter = max(diameter, left + right)

            # return height of this subtree
            return 1 + max(left, right)

        dfs(root)
        return diameter




        
            