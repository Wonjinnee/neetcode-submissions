# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # global variable for dfs function

        def dfs(curr):
            # base case:
            if not curr:
                return 0

            left = dfs(curr.left) # height of the left subtree
            right = dfs(curr.right) # height of the right subtree

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res