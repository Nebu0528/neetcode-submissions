class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for i in range(len(nums)):
            while queue and queue[0] <= i-k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k-1:
                res.append(nums[queue[0]])
        
        return res

        #pseudo code is to have a queue and a res array

        #iterate through nums

        #one whileloop to ensure that the first index in the queue is within the window

        #another queue is to pop from the right so that we are left with the largest element only

        # if the index we append is >= k-1, it's our largest and we append that

