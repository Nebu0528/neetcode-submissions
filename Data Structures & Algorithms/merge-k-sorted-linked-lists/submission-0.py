# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #if we were to use a minheap
        min_heap = []
        #counter to work as a tie breaker
        counter = 0

        for li in lists:
            if li is not None:
                heapq.heappush(min_heap, (li.val, counter, li))
                counter += 1
        
        dummy = ListNode(val=0)
        c = dummy
        while min_heap:
            val, counter, node = heapq.heappop(min_heap)
            c.next = node

            c = c.next

            if c.next is not None:
                heapq.heappush(min_heap, (c.next.val, counter, c.next))
        
        return dummy.next