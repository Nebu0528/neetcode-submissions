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
        #hashmap that contains the old head to the new node
        if head is None:
            return None
        hashmap = {}

        curr = head

        while curr:
            hashmap[curr] = Node(x = curr.val)
            curr = curr.next
        
        # {3*: 3}

        curr = head
        while curr:
            new_node = hashmap[curr]
            if curr.next:
                new_node.next = hashmap[curr.next]
            if curr.random:
                new_node.random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]
        