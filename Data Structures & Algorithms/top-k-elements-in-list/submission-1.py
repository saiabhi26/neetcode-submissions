class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        countList = []
        for key in cnt:
            countList.append([cnt[key],key])
        
        countList.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(countList[i][1])
        return ans

        

