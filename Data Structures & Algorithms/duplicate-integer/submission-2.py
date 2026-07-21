class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        for key, value in seen.items():
            if value >= 2:
                return True
        
        return False

