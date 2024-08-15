# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._inorder_nodes = deque()
        self._left_most(root)
        print(self._inorder_nodes)
        
    def _left_most(self, root):
        if not root:
            return None

        self._inorder_nodes.append(root)
        node = root
        while node.left:
            node = node.left
            self._inorder_nodes.append(node)
        return None

    def next(self) -> int:
        node = self._inorder_nodes.pop()
        if node.right:
            self._left_most(node.right)
        return node.val
        
    def hasNext(self) -> bool:
        if self._inorder_nodes:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()