class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
            else:
                res.append([start,end])

        return res