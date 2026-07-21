"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        start = node
        hashmap = {}
        visited = set()
        visited.add(start)
        stack = []
        stack.append(start)
        if node is None:
            return None

        while stack:
            node = stack.pop()
            hashmap[node] = Node(val = node.val)

            for neighbors in node.neighbors:
                if neighbors not in visited:
                    stack.append(neighbors)
                    visited.add(neighbors)
        
        for old_node, new_node in hashmap.items():
            for neighbors in old_node.neighbors:
                new_neighbor = hashmap[neighbors]
                new_node.neighbors.append(new_neighbor)
        
        return hashmap[start]
        


        


        