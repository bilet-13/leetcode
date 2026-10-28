# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        depth = 0
        queue = deque()
        queue.append(root)

        while queue:
            level = len(queue)
            depth += 1
            for _ in range(level):
                node = queue.popleft()
                if node is None:
                    continue
                if node.left is None and node.right is None:
                    return depth 
                queue.append(node.left)
                queue.append(node.right)
        
        return depth
        