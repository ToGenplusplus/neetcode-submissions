class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
            s1 = "abc", s2 = "lecabee"

            frequency of first len(s1) 3 chars in s2
            s1: a1b1c1, s2:l1e1c1 - not equal

            start processing s2 from index 1 - 1 + len(s1) (3), 4

            start , end, frequency, == s1
            1, 3
        """
        
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[ i - len(s1)]) - ord('a')] -= 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

            if s1_counts == s2_counts:
                return True

        return False



