# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
          
        # traversal the tree if the node we vistied is not a leaf if val < node.val go left else go right
        # unhtil we find the node whidch does not have left/right child wehn we go left/right then inser it 
        # time complexity o(n) n is the number of nodes in the tree
        if root is None:
            return TreeNode(val=val)

        def insert(node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                else:
                    insert(node.left, val)

            else:
                if node.right is None:
                    node.right = TreeNode(val=val)
                else:
                    insert(node.right, val)

        insert(root, val)

        return root


         
        