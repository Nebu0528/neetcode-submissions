class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        cur_sum = 0
        total = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            target = cur_sum-k

            if target in seen:
                total += seen[target]
            seen[cur_sum] = seen.get(cur_sum,0)+1
        
        return total
        