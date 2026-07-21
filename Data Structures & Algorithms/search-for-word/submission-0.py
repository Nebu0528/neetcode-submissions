class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            #if we get the word length, then we built a word
            if i == len(word):
                return True
            
            if (
                r < 0
                or c < 0
                or r >= len(board)
                or c >= len(board[0])
                or word[i] != board[r][c]
                or board[r][c] == "#"
            ):
                return False
            
            #mark the location as visited
            board[r][c] = "#"

            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = word[i]
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

            
        