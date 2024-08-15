# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        preorder = deque()

        self._find_preorder(root, preorder)
        node = root
        preorder.popleft()

        while preorder:
            next_node =  preorder.popleft()
            node.left = None
            node.right = next_node
            node = next_node
        
        return root

    def _find_preorder(self, root, preorder):
        if not root:
            return None


        preorder.append(root)
        self._find_preorder(root.left, preorder)
        self._find_preorder(root.right, preorder)
