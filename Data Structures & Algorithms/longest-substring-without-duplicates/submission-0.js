class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        /**
         what type of chars are in s
         how small / large can s be?
         can s contain spaces?
         expected time and space complexity?

         examples
         s= zxyzxyz -> 3

         s=xxxx -> 1

         s= zxyzxyz
         z - l=1
         zx - l=2
         zxy - l=3
         zxyz - l=3 duplicate char
            z already seen in current window
            need to shrink the window by increasing the left side by 1
            from the first occurence of z in current window

        xyzx - l=3
            duplicate occurence of x
            get position of first occurence of x
            left of window is = occurence + 1
         */

        /**
        o(n) solution
        need a hashmap to track char to index in current window
        two pointes left and right to create a window
        right always moves by 1 on each iteration
        if s[right] is not duplicate right++
        if s[right] is duplicate
            maxLength = max(currMax, right - left - 1)
            left = hash[s[right]] + 1
            hash[s[right]] = right

        keep iterating until right reaches end of string
        return maxLength
         */

        let charWindow = {}

        let left = 0

        let longest = 0
   
        for (let right = 0; right < s.length; right++) {
            if (charWindow[s[right]] !== undefined && charWindow[s[right]] >= left) {
                left = charWindow[s[right]] + 1
            }

            charWindow[s[right]] = right
            longest = Math.max(longest, right - left + 1)
        }

        return longest
    }
}
