class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*(-1)
        heapq.heapify(stones)
        minheap = stones
        while len(minheap) > 1:
            x = heapq.heappop(minheap)
            y = heapq.heappop(minheap)
            smash = x-y
            if smash != 0:
                heapq.heappush(minheap,smash)
        if len(minheap) == 1:
            return -1*minheap[0]
        return 0