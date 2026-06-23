"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i : i.start)
        min_heap = []

        for item in intervals:
            if min_heap and min_heap[0] <= item.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,item.end)
        
        return len(min_heap)
