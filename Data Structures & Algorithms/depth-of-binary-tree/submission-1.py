# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # 1. recursive
        # if not root: # if the root is null
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDept(root.right))

        # # 2. breath first search 
        # if not root:
        #     return 0
        
        # level = 1
        # q = deque([root])
        # while q: # while q is not empty
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level 

        # 3. depth first search
        
        stack = [[root,1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node: # if it's not null
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

