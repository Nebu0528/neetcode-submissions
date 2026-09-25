class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        time = 0
        fresh_o = 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [ [0,1], [0,-1], [1,0], [-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_o += 1
                
                #add rotting oranges
                if grid[r][c] == 2:
                    q.append((r,c))
                
        
        # we want to check while we have rotting oranges and fresh oranges
        while q and fresh_o > 0:
            
            #goes through all rotten oranges in 1 unit of time (since we check adjacent oranges simultaneously)
            for i in range(len(q)):
                # add adjacent oranges
                r, c = q.popleft()

                for dr, dc in directions:
                    row = dr+r
                    col = dc+c

                    #check if inbound and non rotten orange
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):

                    #mark as rotten for fresh oranges

                        grid[row][col] = 2

                        q.append((row,col))
                        fresh_o -= 1
            time += 1
        

        return time if fresh_o == 0 else - 1

