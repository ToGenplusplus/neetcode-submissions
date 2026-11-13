from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        t_counts = Counter(t)
        window = defaultdict(int)
        match = 0

        left = 0

        res = (float('inf'), 0, len(s))

        for right in range(len(s)):

            char = s[right]
            if char in t_counts:
                window[char] += 1
                if window[char] == t_counts[char]:
                    match += 1

            while match == len(t_counts):
                length = right - left + 1
                if length < res[0]:
                    res = (length, left, right + 1)

                char = s[left]
                if char in t_counts:
                    window[char] -= 1

                    if window[char] < t_counts[char]:
                        match -= 1

                left += 1

        return s[res[1] :res[2]] if res[0] != float('inf') else ""
        """
            s = "OUZODYXAZV", t = "XYZ"
            t + X1,Y1,Z1 = total = 3 chars
            match = 0
            O
            OU
            OUZ
                Z is in t and t[z] = 1
                match += 1 = 1
            OUZO
            OUZOD
            OUZODY
                Y is in t and t[Y] = 1
                match += 1 = 2
            OUZODYX
                X is in t and t[x] = 1
                match += 1 = 3
                match = total - this is a valid substring, 
                lenght = 7, min lenght so far,
                reduce from left until invalid
                    left += 1 = 1 - still valid, 7 - 1 = 6, new min length
                    left += 1 = 2 - still valid, 7 - 2 = 5, new min length
                    left += 1 = 3 - no longer valid
                        match -= 1
            0DYXA
            0DYXAZ
                Z is in t and t[z] = 1
                match += 1 = total
                length = 6, reduce from left
                DYXAZ - stil valid
                YXAZ - still valid, min length 4 
                XAZ - no longer valid
        """