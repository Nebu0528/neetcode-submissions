class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_num = 0
        for num in nums:
            if cur_num < 0:
                cur_num = 0
            cur_num += num
            max_sum = max(max_sum, cur_num)
        
        return max_sum
