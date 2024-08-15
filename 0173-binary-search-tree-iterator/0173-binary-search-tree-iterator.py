# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    _inorder_list = []
    _index = None

    def __init__(self, root: Optional[TreeNode]):
        self._inorder_nodes = []
        self._inorder_nodes.append(-1)
        self._index = 0
        self._inorder_search(root)
        
    def _inorder_search(self, root):
        if not root:
            return root

        self._inorder_search(root.left)
        self._inorder_nodes.append(root.val)
        self._inorder_search(root.right)

    def next(self) -> int:
        self._index += 1
        if self._index < len(self._inorder_nodes):
            return self._inorder_nodes[self._index]

    def hasNext(self) -> bool:
        if self._index + 1 < len(self._inorder_nodes):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()