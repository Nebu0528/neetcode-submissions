class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(s):
            i = 0
            j = len(s)-1

            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            
            return True
        
        res = []
        cur_sol = []
        def backtrack(i):
            if i == len(s):
                res.append(cur_sol.copy())
                return
            
            for c in range(i, len(s)):
                if palindrome(s[i:c+1]):
                    cur_sol.append(s[i:c+1])
                    backtrack(c+1)
                    cur_sol.pop()
            
        backtrack(0)

        return res
        