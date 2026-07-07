class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        def process(cur):
            l = 0
            while cur in myset:
                l+=1
                cur+=1
            return l

        myset = set()
        for num in nums:
            myset.add(num)
        
        res = 0
        for num in nums:
            if num-1 not in myset:
                res = max(res,process(num))
        return res