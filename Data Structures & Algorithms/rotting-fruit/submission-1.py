class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
        
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        t = 0

        def addtoq(i,j):
            if min(i,j) < 0 or i == rows or j == cols or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append([i,j])

        while q:
            t+=1
            for k in range(len(q)):
                i, j = q.popleft()
                for x, y in dirs:
                    addtoq(i+x,j+y)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        if t == 0:
            return 0
        return t-1