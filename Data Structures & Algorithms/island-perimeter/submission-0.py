class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            #find an edge
            perimeter = 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            
            if (r,c) in visited:
                return 0
            
            #add to the visited set
            visited.add((r,c))

            for dr, dc in directions:
                perimeter += dfs(dr+r, dc+c)
            
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c)
        
        return 0



            
        