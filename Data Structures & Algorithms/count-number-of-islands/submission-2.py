class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(i,j):
            if min(i,j) < 0 or i >= n or j>=m or grid[i][j] == "0" or (i,j) in visited:
                return
            visited.add((i,j))
            for x, y in dir:
                dfs(i+x,j+y)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res+=1
        return res