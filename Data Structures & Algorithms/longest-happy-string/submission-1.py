class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # cannot be aaa bbb ccc

        hashmap = {
            'a' : a,
            'b' : b,
            'c' : c
        }
        res = []
        
        max_heap = []

        for char, count in hashmap.items():
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            # we should check to see if we already have a consecutive sequence
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                
                # get second most char from heap
                count2, char2 = heapq.heappop(max_heap)

                # increment (essentially decrementing the char)
                #append the char
                res.append(char2)
                count2 += 1

                #if we still have more char2
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                
                #append the first popped char back to use next time
                heapq.heappush(max_heap, (count,char))
            else:
                res.append(char)
                count +=1
                if count < 0:
                    heapq.heappush(max_heap, (count,char))
  
        
        return "".join(res)




