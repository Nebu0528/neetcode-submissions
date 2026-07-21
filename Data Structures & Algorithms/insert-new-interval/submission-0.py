class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []

        #add any intervals that come before newInternval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        #compute a new interval for overlapping ones

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]
            i += 1
        res.append(newInterval)

        #add the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

        