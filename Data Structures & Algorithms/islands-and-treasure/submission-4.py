class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visited = set()
        
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        
        def addtoq(i,j):
            if min(i,j) < 0 or i == n or j == m or grid[i][j] == -1 or (i,j) in visited:
                return
            visited.add((i,j))
            q.append([i,j])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        d = 0
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = d
                for x, y in dirs:
                    addtoq(i+x,j+y)
            d+=1
        
            


        