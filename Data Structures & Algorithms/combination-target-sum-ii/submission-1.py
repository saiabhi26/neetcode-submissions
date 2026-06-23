class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        myset = set()
        candidates.sort()
        def process(i,cur,cursum):
            if cursum == target:
                myset.add(tuple(cur.copy()))
                return
            if cursum > target or i >= len(candidates):
                return
            cur.append(candidates[i])
            process(i+1,cur,cursum+candidates[i])
            cur.pop()
            process(i+1,cur,cursum)
        process(0,[],0)
        res = []
        for item in myset:
            res.append(list(item))
        return res