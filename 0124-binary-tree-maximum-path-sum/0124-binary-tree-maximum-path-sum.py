# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = []
        self.maxPath(root, result)
        
        return result[0]

    def maxPath(self, root, result):
        if root == None:
            return 0
        left_gain = max(self.maxPath(root.left, result), 0)
        right_gain = max(self.maxPath(root.right, result), 0)

        root_sum = root.val + left_gain + right_gain

        if result == []:
            result.append(root_sum)
        elif root_sum > result[0]:
            result[0] = root_sum

        return root.val + max(left_gain, right_gain) 