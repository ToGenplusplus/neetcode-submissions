class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s

        def expand_outer(left, right) -> [int, int]:

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1

            return left + 1, right - 1

        end = start = 0

        for i in range(len(s)):
            #odd
            l,r = expand_outer(i, i)
            if r - l > end - start:
                start, end = l, r


            l,r = expand_outer(i, i + 1)
            if r - l > end - start:
                start, end = l, r

        return s[start: end + 1]
    
        """
            brute force is O(n^3)
            generate every substring - O(n^2)
            check if substring is palindrome = O(n^1)
            O(n^2) * O(n) = O(n^3)

            Interview optimal:

            expand outwards from center
               s is odd, center is a single character
               s is even, center is two characters

            example: s = "ababd"

            0 , a
                i - 1 = -1
                i + 1 = 1
                    -1 is invalid, return i

            a,b
                not equal, return

        """