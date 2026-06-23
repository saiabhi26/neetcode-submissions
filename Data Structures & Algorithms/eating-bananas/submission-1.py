class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end

        while start <= end:
            mid = start + ((end-start)//2)
            hrs = 0
            for i in piles:
                hrs += math.ceil(i/mid)
            if hrs <= h:
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res