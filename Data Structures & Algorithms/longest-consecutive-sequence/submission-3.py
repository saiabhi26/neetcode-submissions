class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        myset = set()
        for num in nums:
            myset.add(num)

        ans = 1
        for num in nums:
            if num - 1 not in myset:
                cur = 0
                while num in myset:
                    cur+=1
                    ans = max(ans,cur)
                    num+=1
        return ans