class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = defaultdict(int)
        for num in nums:
            cnt[num]+=1
        
        minheap = []
        for key in cnt:
            heapq.heappush(minheap,[-cnt[key],key])

        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res

        

