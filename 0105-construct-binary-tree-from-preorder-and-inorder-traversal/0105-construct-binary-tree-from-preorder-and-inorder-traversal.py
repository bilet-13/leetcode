# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def build_map(self, vals):
        index_map = { val: i for i, val in enumerate(vals)}

        return index_map


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = self.build_map(inorder)
        return self._buildTree(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1, index_map)
    
    def _buildTree(self, preorder: List[int], inorder: List[int], pre_start, pre_end, in_start, in_end, index_map):

        if pre_start > pre_end or in_start > in_end:
            return None

        root = TreeNode(val=preorder[pre_start])
        in_root_index = index_map[root.val]
        left_subtree_size = in_root_index - in_start
        
        root.left = self._buildTree(preorder, inorder, pre_start+1, pre_start+left_subtree_size, in_start, in_root_index-1, index_map)
        root.right = self._buildTree(preorder, inorder, pre_start+left_subtree_size+1, pre_end, in_root_index+1, in_end, index_map)

        return root