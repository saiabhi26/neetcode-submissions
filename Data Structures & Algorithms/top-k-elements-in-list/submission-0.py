class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        b = [[] for i in range(len(nums)+1)]
        for key in d:
            b[d[key]].append(key)
        ans = []
        for i in range(len(b)-1,-1,-1):
            if len(ans)==k:
                    break
            for j in range(len(b[i])):
                ans.append(b[i][j])
                if len(ans)==k:
                    break
        return ans
        

