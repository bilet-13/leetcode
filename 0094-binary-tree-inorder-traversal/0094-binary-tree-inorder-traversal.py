# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left child , node, right child
        def _inorder(node, result):
            if node is None:
                return
            
            _inorder(node.left, result)
            result.append(node.val)
            _inorder(node.right, result)

        result = []
        _inorder(root, result)

        return result
