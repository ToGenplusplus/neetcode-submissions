class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        """
            Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

            [1,3]
                2 <= 3
                merged = min(1,2),max(3,5) = [1,5]
            [4,6]
                4 <= 5
                merged = min(1,4), max(5,6) = [1,6]
            done processing, add [1,6] to result


            [[1,2],[3,5],[9,10]], newInterval = [6,7]
            [1,2]
                2 < 6, add [1,2] to result
            [3,5]
                5 < 6, add [3,5] to result
            i = 2, [9,10]
                7 < 9,
                add [6,7] to res

            exit loop, add remainder of elements in nums from i onward into res
        """

        res = []

        i = 0
        merged = newInterval

        while i < len(intervals):
            if intervals[i][1] < merged[0]:
                res.append(intervals[i])
            elif intervals[i][0] <= merged[1]:
                merged = [min(intervals[i][0], merged[0]), max(intervals[i][1], merged[1])]
            elif intervals[i][0] > merged[0]:
                res.append(merged)
                break
            
            i+=1

        if i < len(intervals):
            res += intervals[i:]
        else:
            res.append(merged)

        return res
