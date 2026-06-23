class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])

        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        t = 0

        def addtoq(i,j):
            if min(i,j) < 0 or i >= n or j>= m or grid[i][j] !=1:
                return
            grid[i][j] = 2
            q.append([i,j])
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                for x, y in dir:
                    addtoq(i+x,j+y)
            t+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        if t == 0:
            return 0
        return t-1




