class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxl = height[l]
        maxr = height[r]
        sumofwater = 0
        
        while l < r:
            if maxl <= maxr:
                l+=1
                w = maxl - height[l]
                if w > 0:
                    sumofwater += w
                maxl = max(maxl,height[l])
            else:
                r-=1
                w = maxr - height[r]
                if w > 0:
                    sumofwater += w
                maxr = max(maxr, height[r])
        return sumofwater