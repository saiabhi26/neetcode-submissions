class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]
        res = []
        i = 0
        while i < len(intervals):
            item = intervals[i]
            start, end = item
            if end < newStart:
                res.append(item)
            elif start <= newEnd:
                newStart = min(start,newStart)
                newEnd = max(end,newEnd)
            else:
                break
            i+=1
        res.append([newStart, newEnd])
        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res
        
            

                