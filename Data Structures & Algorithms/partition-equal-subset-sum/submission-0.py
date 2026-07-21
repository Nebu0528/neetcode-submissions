class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #can't compute for an odd integer number
        if sum(nums) % 2 == 1:
            return False
        
        total = sum(nums) // 2

        dp = [False] * (total+1)
        dp[0] = True

        for n in nums:
            for i in range(len(dp)-1, n-1, -1):
                if dp[i]: continue
                if dp[i-n]: dp[i] = True
                if dp[-1]: return True
        
        return False
        