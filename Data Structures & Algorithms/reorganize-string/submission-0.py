class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)
        res = []
        heap = []
        
        for c in s:
            hashmap[c] += 1
        
        #build out a max heap
        for char, count in hashmap.items():
            heapq.heappush(heap, (-count, char))
        
        #use prev to keep track of chars used
        prev = None
        while heap or prev:
            if not heap and prev:
                return ""
            

            count, char = heapq.heappop(heap)
            #append to res
            res.append(char)
            #decrement the count, since we use neg values we add to decrement
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            #if the count for the char is not 0, we still have to use it so
            if count != 0:
                prev = (count, char)
            
        return "".join(res)
            
