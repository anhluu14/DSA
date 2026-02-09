class Solution:
    #grid 2D nao cung can ham nay
    def isInsideGrid(self, row: int, col: int) -> bool:
        #row nam trong khoang 0 toi m - 1
        return (row >= 0 and row <= self.m - 1 and col >= 0 and col <= self.n - 1)
    
    def DFS(self, row: int, col: int):
        self.visited[row][col] = True
        for direction in range(4):
            new_row = row + self.dX[direction]
            new_col = col + self.dY[direction]

            #check if (new row, new col) is valid?
            #check water or land
            if self.isInsideGrid(new_row, new_col) and self.grid[new_row][new_col] == "1" and self.visited[new_row][new_col] == False:
                self.DFS(new_row, new_col)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        
        #current DFS in (row, col)
        #bien thien cua
        # (row, col) -> (row - 1, col): up
        #            -> (row, col -1): left
        #            -> (row + 1, col): down
        self.dX = [-1, 0, 0, 1] #di len tren
        self.dY = [0, -1, 1, 0]

        connected_component = 0
        for row in range(self.m):
            for col in range(self.n):
                if self.grid[row][col] == "1" and self.visited[row][col] == False:

                    connected_component += 1
                    self.DFS(row,col)
        
        return connected_component