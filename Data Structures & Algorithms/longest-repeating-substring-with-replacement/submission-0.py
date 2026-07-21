class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            curr_window = right-left+1
            max_values = max(freq.values())

            if curr_window - max_values > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = right-left+1
        
        return max_len

                
            
        