class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def process(i, arr):
            if i < len(nums):
                arr.append(nums[i])
                process(i+1, arr)
                arr.pop()
                process(i+1, arr)
            else:
                res.append(arr[::])
            
        process(0, [])
        return res