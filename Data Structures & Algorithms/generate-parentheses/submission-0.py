class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open_p, closed_p):
            if open_p+closed_p == 2*n:
                res.append("".join(cur))
                return
            
            if open_p < n:
                cur.append("(")
                backtrack(open_p+1, closed_p)
                cur.pop()

            if closed_p < open_p:
                cur.append(")")
                backtrack(open_p, closed_p+1)
                cur.pop()
            
        backtrack(0,0)
        return res
        