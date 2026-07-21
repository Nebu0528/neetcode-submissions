class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by starting time
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        merged = []
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        return merged



        