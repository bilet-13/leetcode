# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
          # 
        #recursive?
        # to many repeatiiton use @cache
        def ask_rob(node):
            if node is None:
                return (0, 0)

            left_rob, left_not_rob = ask_rob(node.left)
            right_rob, right_not_rob = ask_rob(node.right)

            node_rob = node.val + left_not_rob + right_not_rob
            node_not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return (node_rob, node_not_rob)
       
        return max(ask_rob(root)) 
        