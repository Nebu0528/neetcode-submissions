class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        heap = []
        for key, value in hashmap.items():
            heapq.heappush(heap, (value, key))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        #print(heap)
        return [value for key, value  in heap]