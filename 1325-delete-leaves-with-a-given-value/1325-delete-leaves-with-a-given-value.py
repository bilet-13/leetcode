# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
         # recursive
        # if node is None return None
        # remove leaf node of left subtree and right subtree
        # check the node become leaf node and node.val == target or not
        # if yes, return None else return root
        # tiem complexity o(n)
        # finally resutnr node

        if root is None:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left is None and root.right is None and root.val == target:
            return None

        return root
        
        