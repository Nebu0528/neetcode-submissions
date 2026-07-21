class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(s):
            i = 0
            j = len(s)-1

            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j -=1
            return True
        
        count = 0
        #create 2 nested for loops
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i: j+1]

                if palindrome(substring):
                    count += 1
        
        return count
        



        