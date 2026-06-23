class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def process(i):
            if i < len(nums):
                cur.append(nums[i])
                process(i+1)
                cur.pop()
                process(i+1)
            else:
                res.append(cur.copy())
            
        process(0)
        return res