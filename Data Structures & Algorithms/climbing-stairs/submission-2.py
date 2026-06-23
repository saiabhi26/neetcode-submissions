class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        s = 1

        for i in range(n-1):
            temp = f
            f = f+s
            s = temp
        return f