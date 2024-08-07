# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        queue = deque()
        queue.append([root, root.val])
        visited = set()
        visited.add(root)
        answer = False

        while queue:
            n,  sum_n = queue.popleft()
            if not n.left and not n.right:
                if sum_n == targetSum:
                    answer |= True
                answer |= False

            for child in [n.left, n.right]:
                if child and child not in visited:
                    queue.append([child, sum_n + child.val])
                    visited.add(child)
        
        return answer
