class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks:
            c = task[0]
            if c in d:
                d[c]+=1
            else:
                d[c] = 1
        maxheap = []
        for key in d:
            heapq.heappush(maxheap,[-(d[key]),key])
        q = []
        t = 0
        while maxheap or q:
            if q and q[0][1] == t:
                heapq.heappush(maxheap,q[0][0])
                q.pop(0)
            if maxheap:
                count, task = heapq.heappop(maxheap)
                count+=1
                if count < 0:
                    q.append([[count,task],t+n+1])
            t+=1
        return t
            
