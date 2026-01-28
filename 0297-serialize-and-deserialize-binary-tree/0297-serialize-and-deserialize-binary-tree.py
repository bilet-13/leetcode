# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:

        result = []

        def dfs(node):
            if node is None:
                result.append('N')
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.idx = 0

        def dfs():
            if vals[self.idx] == 'N':
                self.idx += 1
                return None
            
            node = TreeNode(val=int(vals[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        
        root = dfs()
        return root

        



