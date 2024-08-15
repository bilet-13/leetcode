# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        
        return self._sumNumbers(root, "")

    def _sumNumbers(self, root, num_path):
        if not root:
            return 0
        
        if not root.left and not root.right:
            num = num_path + str(root.val)
            return int(num)

        left_sum = self._sumNumbers(root.left, num_path+str(root.val))
        right_sum = self._sumNumbers(root.right, num_path+str(root.val))
        return left_sum + right_sum