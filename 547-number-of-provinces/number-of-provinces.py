class Solution:
    def DFS(self, u: int):
        self.visited[u] = True

        for v in range(self.n):
            if self.isConnected[u][v] == 1 and self.visited[v] == False:
                self.DFS(v)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        self.isConnected = isConnected
        self.visited = [False] * self.n #kiem soat cac dinh da di qua
        connected_component = 0
        for u in range(self.n):
            if self.visited[u] == False:
                connected_component += 1
                self.DFS(u)
        return connected_component