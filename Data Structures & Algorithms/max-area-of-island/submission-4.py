class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        maxarea = 0

        def dfs(i,j,area):
            area[0] += 1
            if i+1 < n and grid[i+1][j] == 1 and (i+1,j) not in visited:
                visited.add((i+1,j))
                dfs(i+1,j,area)
            if i-1 >= 0 and grid[i-1][j] == 1 and (i-1,j) not in visited:
                visited.add((i-1,j))
                dfs(i-1,j,area)
            if j+1 < m and grid[i][j+1] == 1 and (i,j+1) not in visited:
                visited.add((i,j+1))
                dfs(i,j+1,area)
            if j-1 >= 0 and grid[i][j-1] == 1 and (i,j-1) not in visited:
                visited.add((i,j-1))
                dfs(i,j-1,area)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = [0]
                    visited.add((i,j))
                    dfs(i,j,area)
                    maxarea = max(area[0],maxarea)
        return maxarea

        

        




