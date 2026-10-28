# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        result = 0
        depth = 0

        def findDepth(node):
            nonlocal depth
            nonlocal result
            if node is None:
                return
            depth += 1
            result = max(result, depth)

            findDepth(node.left)
            findDepth(node.right)
            depth -= 1
        
        findDepth(root)
        return result
        