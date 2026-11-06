# my solution
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        s_window = defaultdict(int)
        t_counts = Counter(t)

        t_total = len(t_counts)
        s_match_t = 0

        left = 0

        min_len = float('inf')
        res_start = 0
        res_end = len(s)

        for right in range(len(s)):
            c = s[right]
            if c in t_counts:
                s_window[c] += 1
                if s_window[c] == t_counts[c]:
                    s_match_t += 1

            while s_match_t == t_total:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    res_start = left
                    res_end = right

                c = s[left]
                if c in t_counts:
                    s_window[c] -= 1
                    if s_window[c] < t_counts[c]:
                        s_match_t -= 1

                left += 1

        return s[res_start:res_end+1] if min_len != float('inf') else ""

        """
            "ZODYXAZ", t = "XYZ"

            t: X->1,Y->1,Z->1

            right, s[right], left, operation,result
            0, Z, 0
                Z is in t,
                t only has 1 Z, 
            1,O,0
            2,D,0
            3,Y,0
                Y is in t
                t only has 1 Y
            4,X,0
                X is in t,
                t only has 1 X
                at subtring = 4 - 0 + 1 = 5 - 5 is smalles so far
                increast left until no longer valid
            5,A,1
            6,Z,1
                Z is in t,
                at substring 6 - 1 + 1 = 6, 5 < 6 discard
                increase left until no longer valid
                left += 1 = 2, 6 - 2 + 1 = 5 
                left += 1 = 3, 6 - 3 + 1 = 4 , 4 < prev min (5)
                left += 1 = 4, no longer valid, exit loop

            exit return - smallest


        """