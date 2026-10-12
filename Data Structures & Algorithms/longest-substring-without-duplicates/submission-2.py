class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            given
                string s
                    lower case english letters
                    len(s) []

            return 
                int - longest substring with distinct characters


            examples
                abbceffg -> 4 (bcef)

            abb
                duplicate - already saw b at position 1
                new window starts from last b poitision + 1
            bceff
                duplicate - already saw f at position 5
                new window starts at 5 + 1 = 6
            fg
                done 
        """

        window = {}

        longest = 0

        left = 0

        for right in range(len(s)):

            char = s[right]
            if char in window and window[char] >= left:
                left = window[char] + 1

            longest = max(longest, right - left + 1)
            window[char] = right
        
        return longest
