class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[n-1] = 1
        i = n-2
        while i >= 0:
            curmax = 1
            j = i+1
            while j < n:
                if nums[j] > nums[i]:
                    curmax = max(curmax, dp[j]+1)
                j+=1
            dp[i] = curmax
            i-=1
        return max(dp)