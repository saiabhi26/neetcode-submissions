class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxl = height[l]
        maxr = height[r]
        maxw = 0
        while l<r:
            if maxl <= maxr:
                l+=1
                w = maxl - height[l]
                if w > 0:
                    maxw += w
                if height[l]>maxl:
                    maxl = height[l]
            else:
                r-=1
                w = maxr - height[r]
                if w > 0:
                    maxw += w
                if height[r]>maxr:
                    maxr = height[r]
        return maxw
            