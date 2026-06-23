class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def process(i,cursum):
            if cursum == target:
                res.append(cur.copy())
                return
            if cursum > target or i >= len(nums):
                return

            cur.append(nums[i])
            process(i,cursum+nums[i])
            cur.pop()
            process(i+1,cursum)
        process(0,0)
        return res