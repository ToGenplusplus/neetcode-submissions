class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []

        largest = 0

        for i, num in enumerate(heights + [0]):

            while stack and heights[stack[-1]] > num:
                l = heights[stack.pop()]

                w = i - stack[-1] - 1 if stack else i

                largest = max(largest, l * w)

            stack.append(i)

        return largest


        """

            heights = [7,1,7,2]

            i, h[i], stack, operation, result
            0,7, [], add i to stack, [0], contine
            1,1,[0], 1 < stack[0](7)
                pop 0 from stack
                stack is empty so area = 7 * i = 7 * 1 = 7
                push index i on stack [1]
            2,7, [1], 7 > s[-1] add index 2 to stack [1,2]
            3,2,[1,2],2 < s[-1](7)
                pop 2 from stack, h[2] is our L in A * w
                width is bounded by s[-1] since s is not empty and current i 3
                A = 7 * (3 - 1 - 1) = 7
                add index 3 to stack, [1,3]
            4,0, 0 < s[3] (2)
                pop 3 from stack, h[3] is 2 = L, s = [1]
                w = 4 - 1 - 1 = 2
                A = 2 * 2 = 4
                stack is not empty and h[s[-1]] (1) > h[i] (0), repeat
                    pop 1 from stack, h[1] is L
                    w = i since s is now empty
                    A = 1 * 4 = 4

                max area is 7             
        """