# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #recursive function for dft
        def bfs(pnode, qnode):
            #base case: if node is null, 
            # Q. how do i solve when
            if not pnode and not qnode:
                return True
            if not pnode or not qnode:
                return False
            if pnode.val == qnode.val:
                return bfs(pnode.left, qnode.left) and bfs(pnode.right, qnode.right)
            else: # if pnode != qnode
                return False

        return bfs(p, q)