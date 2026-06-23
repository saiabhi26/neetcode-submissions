class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxheap = []
        for x,y in points:
            d = -(x**2 + y**2)
            heapq.heappush(maxheap,[d,x,y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        res = []
        while maxheap:
             d, x, y = heapq.heappop(maxheap)
             res.append([x,y])
        return res