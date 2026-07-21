class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_seq = 0

        for num in nums:
            if num-1 not in seen:
                length = 1

                while num+length in seen:
                    length +=1
                longest_seq = max(length, longest_seq)
        
        return longest_seq
        