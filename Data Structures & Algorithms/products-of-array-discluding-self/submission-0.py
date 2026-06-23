class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        suf=[]
        product=1
        for i in nums:
            pre.append(product)
            product=product*i
        product=1
        for i in range(len(nums)-1,-1,-1):
            suf.append(product)
            product=product*nums[i]
        ans=[]
        for i in range(len(suf)):
            ans.append(pre[i]*suf[len(suf)-1-i])
        return ans