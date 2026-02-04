class Solution:
    def dfs(self, u: int):
        self.visited[u] = True

        for v in self.adj[u]:
            if self.visited[v] == True:
                continue
            
            self.dfs(v)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.n = n
        self.adj = [[] for _ in range(n)]
        # convert list edges -> adjacent list
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]

            self.adj[u].append(v)
            self.adj[v].append(u)

        # DFS initilization
        self.visited = [False] * n

        # DFS
        self.dfs(source)

        #check if source can reach destination
        if self.visited[destination] == True:
            return True
        else:
            return False