class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j):
            if min(i,j) < 0 or i == rows or j == cols or board[i][j] != "O":
                return
            board[i][j] = "#"
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for x, y in dirs:
                dfs(i+x,j+y)    

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][cols-1] == "O":
                dfs(i,cols-1)
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0,j)
            if board[rows-1][j] == "O":
                dfs(rows-1,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
            
        
        