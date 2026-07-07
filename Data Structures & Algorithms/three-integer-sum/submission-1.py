class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        myset = set()
        res = []

        for i in range(len(nums)):
            num = nums[i]
            if num > 0:
                break
            if num in myset:
                continue
            myset.add(num)
            l = i+1
            r = len(nums)-1

            while l < r:
                left = nums[l]
                right = nums[r]
                
                if left + right + num > 0:
                    r-=1
                elif left + right + num < 0:
                    l+=1
                else:
                    res.append([num, left, right])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res

