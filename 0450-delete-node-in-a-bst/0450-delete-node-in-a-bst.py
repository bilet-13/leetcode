# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            max_in_left_tree = self.find_max(root.left)

            root.val = max_in_left_tree.val

            root.left = self.deleteNode(root.left, max_in_left_tree.val)

        return root

    
    def find_max(self, root):
        while root.right:
            root = root.right

        return root


        