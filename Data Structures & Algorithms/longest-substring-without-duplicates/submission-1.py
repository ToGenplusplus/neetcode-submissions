class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            examples
            s = "zxyzxyz"
            z
            zx
            zxy
            zxyz - longest = 3, z already seen at index 0, increase lookup window
            xyzx - long = 3, x already seen at index 1

            constraints
            how long can s be
            what type of characters does s have
            time and space complexity constraints?
        """

        char_window = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in char_window and char_window[s[right]] >= left:
                left = char_window[s[right]] + 1
            else:
                longest = max(longest, right - left + 1)
            char_window[s[right]] = right

        return longest
        