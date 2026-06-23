class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            d={}
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]]=1    
        for i in range(9):
            d={}
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in d:
                        return False
                    else:
                        d[board[j][i]]=1
        d={}
        for i in range(3):
            for j in range(3):
                d[tuple([i,j])]=[]
        for i in range(9):
            m = i//3
            for j in range(9):
                n = j//3
                if board[i][j]!=".":
                    if board[i][j] in d[(m,n)]:
                        return False
                    else:
                        d[(m,n)].append(board[i][j])
        return True
        