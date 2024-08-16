# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif not root.left and not root.right:
            return root.val

        left_path_sum = self.maxPathSumRoot(root.left)
        right_path_sum = self.maxPathSumRoot(root.right)
        root_max_path = root.val + (left_path_sum if left_path_sum > 0 else 0) + (right_path_sum if right_path_sum > 0 else 0)
        
        paths = [root_max_path]
        if root.left:
            left_sub_max = self.maxPathSum(root.left)
            paths.append(left_sub_max)
        if root.right:
            right_sum_max = self.maxPathSum(root.right)
            paths.append(right_sum_max)
        return max(paths)

    def maxPathSumRoot(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.val

        return root.val + max(self.maxPathSumRoot(root.left), self.maxPathSumRoot(root.right), 0)

        