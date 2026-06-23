class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        for i in nums:
            d[i]=1
        maxl = 1
        for i in nums:
            l = 1
            if i-1 not in d:
                n = i
                while n+1 in d:
                    l+=1
                    n+=1
            maxl = max(maxl, l)
        return maxl
