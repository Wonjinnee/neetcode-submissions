# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursively invert the tree
        # 내 1차 풀이 6/21
        # while root:
        #     L = root.left     
        #     R = root.right
        #     root.left = R
        #     root.right = L
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return self

        if not root: # if the element is not at the tree
            return None
        # swap the children
        L = root.left     
        R = root.right
        root.left = R
        root.right = L

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

