class Solution:
    def isInsideGrid(self, row: int, col: int):
        return row >= 0 and row <= self.n - 1 and col >= 0 and col <= self.n - 1
    def BFS(self):
        if self.grid[0][0] == 1:
            return -1
        #tim duong di ngan nhat tu source to sink
        dX = [-1, -1, -1, 0, 0, 1, 1, 1]
        dY = [-1, 0, 1, -1, 1, -1, 0, 1]

        # d[v] la duong di ngan nhat tu source toi v
        # d[v] = -1 -> dinh v chua duoc visited
        d = [[-1 for _ in range(self.n)] for _ in range (self.n)]
        d[0][0] = 0

        queue = deque()
        queue.append([0, 0])

        while len(queue) > 0:
            cell = queue.popleft() #lay cac dinh dau tien ra khoi queue
            row = cell[0]
            col = cell[1]

            for direction in range(8):
                new_row = row + dX[direction]
                new_col = col + dY[direction]

                if self.isInsideGrid(new_row, new_col) and self.grid[new_row][new_col] == 0 and d[new_row][new_col] == -1:
                    d[new_row][new_col] = d[row][col] + 1
                    queue.append([new_row, new_col])
                    
        if d[self.n - 1][self.n - 1] == -1:
            return -1
        else:
            return d[self.n - 1][self.n - 1] + 1 #tinh dinh xuat phat luon

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.grid = grid

        return self.BFS() 