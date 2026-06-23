class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow = 0
        rrow = len(matrix)-1
        while lrow <= rrow:
            midrow = lrow + ((rrow-lrow)//2)
            if target < matrix[midrow][0]:
                rrow = midrow-1
            elif target > matrix[midrow][len(matrix[midrow])-1]:
                lrow = midrow+1
            else:
                start = 0
                end = len(matrix[midrow])-1
                while start <= end:
                    mid = start + ((end-start)//2)
                    if target == matrix[midrow][mid]:
                        return True
                    elif target < matrix[midrow][mid]:
                        end = mid-1
                    else:
                        start = mid+1
                return False
        return False
            