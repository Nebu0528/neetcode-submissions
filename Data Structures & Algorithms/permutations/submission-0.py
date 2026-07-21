class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_comb = []

        def backtrack(cur_comb):
            if len(cur_comb) == len(nums):
                res.append(cur_comb.copy())
                return
            
            for num in nums:
                if num not in cur_comb:
                    cur_comb.append(num)
                    backtrack(cur_comb)
                    cur_comb.pop()
        
        backtrack([])
    
        return res
        