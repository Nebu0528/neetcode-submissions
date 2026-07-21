class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r, c):
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                grid[r][c] != "1" or
                (r, c) in visited
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands
