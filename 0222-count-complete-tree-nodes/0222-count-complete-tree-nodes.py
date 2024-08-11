# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.right:
            return 1 + self.countNodes(root.left)

        left_most_depth = self.get_depth(root)
        right_most_depth = self.get_depth(root, True)

        if left_most_depth == right_most_depth:
            return self.calculateNodes(root, left_most_depth)
        else:
            left = root.left
            left_left_most_depth = self.get_depth(left)
            left_right_most_depth = self.get_depth(left, True)

            if left_left_most_depth == left_right_most_depth:
                return 1 + self.calculateNodes(root.left, left_left_most_depth) + self.countNodes(root.right)
            else:
                return 1  + self.calculateNodes(root.right, right_most_depth-1) + self.countNodes(root.left)
    
    def get_depth(self, root, rightmost=False):
        if not root:
            return 0
        depth = 0
        if not rightmost:
            root = root.left
        else:
            root = root.right
        while root:
            depth += 1
            if not rightmost:
                root = root.left
            else:
                root = root.right
        return depth
    def calculateNodes(self, root, depth):
        if not root:
            return 0
        else:
            return sum([2**i for i in range(0, depth+1)])