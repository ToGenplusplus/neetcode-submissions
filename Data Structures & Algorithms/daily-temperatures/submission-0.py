class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
            
            i | t[i] | s [] | r
            0 | 30 | [0]
            1, 38, 38 > t[-1]
                need_warmer = t.pop
                res[need_warmer] = i - need_warmer
                res = [1], s[1]
            2, 30, s[1, 2]
            3, 36, 36 > t[-1]
                need_warmer = t.pop
                res[need_warmer] = i - need_warmer
                res = [1], s[1]

        """

        s = []

        t = len(temperatures)
        res = [0] * t

        for i in range(t):
            while s and temperatures[i] > temperatures[s[-1]]:
                need_warmer = s.pop()
                res[need_warmer] = i - need_warmer

            s.append(i)

        return res


        