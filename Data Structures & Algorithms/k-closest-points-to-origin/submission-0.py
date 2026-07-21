import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #min heap
        heap = []
        for point in points:
            val = math.sqrt((point[0]**2)+(point[1]**2))
            heapq.heappush(heap, (-val, point))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [point for val, point in heap]