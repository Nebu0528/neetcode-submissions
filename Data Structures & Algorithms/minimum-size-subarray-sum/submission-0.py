class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window approach
        left = 0
        cur_sum = 0
        min_len = math.inf

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(right-left+1, min_len)
                cur_sum -= nums[left]
                left += 1

        
        return 0 if min_len == math.inf else min_len




            


        