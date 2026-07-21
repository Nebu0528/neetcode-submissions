class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # keep a hashmap of the values and freqs
        #append the first character, add cooldown of n if you must have the same n tasks next to each other
        #then pop from the heap
        #append the next value, then 

        count = Counter(tasks)

        max_heap = [-cnt for cnt in count.values()]
        #heapify to get a max heap
        heapq.heapify(max_heap)

        time = 0
        #contains a pair of values -cnt and time that the task can be next processed
        queue = deque()
        
        while max_heap or queue:
            time +=1

            if max_heap:
                #pop from it
                #since we have negatives value, to decrement the count we add 1
                cnt = 1 + heapq.heappop(max_heap)
                #if we have a count, append the value to the queue 
                #add the count and the time the task is available to be processed
                if cnt:
                    queue.append([cnt, time+n])
            
            #check if the first element from the queue and if the time it's available for matches
            #the time
            if queue and queue[0][1] == time:
                #add it back to max_heap
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time
        





                