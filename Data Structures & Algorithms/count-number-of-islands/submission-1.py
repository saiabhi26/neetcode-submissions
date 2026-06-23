class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            if i+1 < n and grid[i+1][j] == "1" and (i+1,j) not in visited:
                visited.add((i+1,j))
                dfs(i+1,j)
            if i-1 >=0 and grid[i-1][j] == "1" and (i-1,j) not in visited:
                visited.add((i-1,j))
                dfs(i-1,j)
            if j+1 < m and grid[i][j+1] == "1" and (i,j+1) not in visited:
                visited.add((i,j+1))
                dfs(i,j+1)
            if j-1 >=0 and grid[i][j-1] == "1" and (i,j-1) not in visited:
                visited.add((i,j-1))
                dfs(i,j-1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    dfs(i,j)
                    res += 1
        return res