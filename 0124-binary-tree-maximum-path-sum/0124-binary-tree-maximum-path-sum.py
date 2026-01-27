# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       
        self.result = -float("inf")

        def find_max(node):
            if node is None:
                return 0
            
            left_max = max(find_max(node.left), 0)
            right_max = max(find_max(node.right), 0)

            self.result = max(self.result, left_max + node.val + right_max)

            return max(left_max + node.val, right_max + node.val)

        find_max(root)

        return self.result

        

         