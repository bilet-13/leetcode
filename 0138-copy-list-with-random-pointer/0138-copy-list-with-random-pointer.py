"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create hash map map index of node to index of random node
        node_to_index = {} # map key: id (node) value: index of the node
        index_to_node = []
        curr = head
        index = 0

        while curr:
            node_to_index[id(curr)] = index
            index_to_node.append(curr)

            curr = curr.next
            index += 1
        
        list_length = index
        dummy = Node(-1)
        copy_nodes = []

        curr = dummy
        original_curr = head

        # 2 create new nodes with same values
        while original_curr:
            curr.next = Node(x=original_curr.val)
            original_curr = original_curr.next
            curr = curr.next

            copy_nodes.append(curr)

        # 3 set up random pointers
        for i in range(list_length):
            random_node = index_to_node[i].random
            copy_nodes[i].random = copy_nodes[node_to_index[id(random_node)]] if random_node is not None else None

        return dummy.next
        