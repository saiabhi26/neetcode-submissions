class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            num = nums[i]
            if num == 0:
                temp = nums[zero]
                nums[zero] = num
                nums[i] = temp
                zero+=1
                i+=1
            elif num == 2:
                temp = nums[two]
                nums[two] = num
                nums[i] = temp
                two-=1
            else:
                i+=1
        
        return nums
                
             