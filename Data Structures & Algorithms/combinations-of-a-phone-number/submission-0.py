class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        if not digits:
            return []
        res = []
        cur_comb = []
        def backtrack(i):
            if len(cur_comb) == len(digits):
                res.append("".join(cur_comb))
                return
            
            letters = hashmap[digits[i]]

            for letter in letters:
                cur_comb.append(letter)
                backtrack(i+1)
                cur_comb.pop()
            
        backtrack(0)
        return res

        