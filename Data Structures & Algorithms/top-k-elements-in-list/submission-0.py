class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        
        heap = []
        for key,value in hashmap.items():
            heapq.heappush(heap, (value, key))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [key for value, key in heap]
        