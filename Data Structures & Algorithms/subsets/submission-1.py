class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        myset = set()
        def process(i,nums,arr,myset):
            if i < len(nums):
                process(i+1,nums,arr + (nums[i],),myset)
                process(i+1,nums,arr,myset)
            myset.add(arr)
            
        process(0,nums,(),myset)
        res = []
        for item in myset:
            res.append(list(item))
        return res