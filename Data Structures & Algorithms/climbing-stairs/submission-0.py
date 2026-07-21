class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            
            result = dfs(i+1) + dfs(i+2)
            cache[i] = result
            return result
        
        return int(dfs(0))
        