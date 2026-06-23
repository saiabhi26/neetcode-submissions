class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        cnt = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                cnt+=1
            else:
                i+=1
        return n-cnt