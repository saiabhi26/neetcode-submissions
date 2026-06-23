class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum1 = max(nums)
        cur = nums[0]
        for num in nums[1:]:
            cur = max(cur,0)
            cur += num
            maxsum1 = max(maxsum1,cur)
        
        minsum = min(nums)
        wholesum = sum(nums)
        cur = nums[0]
        for num in nums[1:]:
            cur = min(cur+num, num)
            minsum = min(minsum, cur)
        if minsum != wholesum:
            maxsum2 = wholesum - minsum
        else:
            return maxsum1
        return max(maxsum1, maxsum2)