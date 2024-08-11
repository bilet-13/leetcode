# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def build_map(self, preorder, inorder):
        index_map = {}
        for i in range(len(preorder)):
            val = preorder[i]
            if val not in index_map:
                index_map[val] = {}
            index_map[val]['pre'] = i
            for j in range(len(inorder)):
                if inorder[j] == val:
                    index_map[val]['in'] = j

        return index_map


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = self.build_map(preorder, inorder)
        print(index_map)
        
        return self._buildTree(preorder, inorder, index_map)
    
    def _buildTree(self, preorder: List[int], inorder: List[int], index_map):
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        
        root = TreeNode(val=preorder[0])
        pre_root_index =  index_map[root.val]['pre']
        in_root_index = inorder.index(root.val)

        root.left = self._buildTree(preorder[1:in_root_index+1], inorder[:in_root_index], index_map)
        root.right = self._buildTree(preorder[in_root_index+1:], inorder[in_root_index+1:], index_map)

        return root