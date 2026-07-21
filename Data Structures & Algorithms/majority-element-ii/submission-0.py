class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        n = len(nums)

        for num in nums:
            hashmap[num] +=1
        
        res = []

        for key,value in hashmap.items():
            n_3 = n // 3

            if value > n_3:
                res.append(key)
        
        return res
            
        