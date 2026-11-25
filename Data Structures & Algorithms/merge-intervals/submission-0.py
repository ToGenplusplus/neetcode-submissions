class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        first we sort based on the end in interval[i]
            [[1,3],[1,5],[6,7]] -> [[1,5], [6,7]]
            [[1,3],[4,5],[6,7]] -> [[1,3],[4,5],[6,7]]

            [[2,3][1,4],[5,8],[6,7]] 
                sorted -> [[2,3][1,4],[6,7],[5,8]] 
                    i, intv[i], operation, result
                    0, [2,3], nothing
                    1, [1,4], 
                        1 is < 3
                        new interval is min(1,2), max(3,4) = 1,4 -push to result
                    2, [6,7],nothing
                    3, [5,8], 5 < 7
                        merge -> [5,8]
                    -> [1,4], [5,8]

            [[2,3][4,5],[6,7],[3,8]] 
            [[2,3][4,5],[3,8]]
            [[2,3], [3,8]] 
            [[2,8]] 

            [[3,8], [6,7], [4,5], [2,3]]
            [[3,8], [4,5], [2,3]]
            [[3,8], [2,3]]
            [[2,8],]
                    
            [[6,8], [6,7], [4,5], [2,3]]
            [[6,8], [4,5], [2,3]]
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x:x[1], reverse=True)

        res = []

        for i in range(0, len(intervals)):
            if res and intervals[i][1] >= res[-1][0]:
                intv = res.pop()
                res.append([min(intervals[i][0], intv[0]), max(intervals[i][1], intv[1])])
            else:
                res.append(intervals[i])

        return res

        """
            [1,3],[1,5],[6,7]]
            [6,7], [1,5], [1,3]

        i, nums[i]
        0, [6,7], add to res
        1, [1,5]
            5 , res[-1][0], add [1,5] to res
        2, [1,3]
            3 >= res[-1][0]
            pop res
        """