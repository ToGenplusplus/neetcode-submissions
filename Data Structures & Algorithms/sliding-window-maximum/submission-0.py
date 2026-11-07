from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()

        res = []

        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
        """
            nums = [1,2,1,0,4], k = 2


            i , window, q, operation, res
            0, [1], [], add i to q, q= [0]
            1, [1,2], [0],
                0 is not < 1 - 2 + 1 = 0
                2 > nums[q[-1]], pop from q, append i, q = [1], res = [2]
            2, [2,1], [1]
                1 is not < 2 - 2 + 1 = 1
                1 < n[q[-1]], append i, q = [1,2], res = [2,2]
            3, [1,0], [1,2]
                1 is < 3 - 2 + 1 = 2, popleft 1 from q, [2]
                0 < n[q[-1]] (1), append i to q = [2,3], app n[q[0]] to res = 2,2,1
            4, [0,4], [2,3]
                2 is < 4 - 2 + 1 = 3, popleft 2 from q, [3]
                4 > n[q[-1]] (0), pop from q,

            [1,2] ->2
            2,1 -> 2
            1,0 -> 1
            0,4 -> 4
            -> [2,2,1,4]


            i | nums[i] | window_elements, max_tracker []|operation, result []
            0 | 1 | [1],[] | insert i into max_tracker, [0]
            1 | 2 | [1,2],[0] |
                2 > nums[m_t[-1]](1)
                pop from m_t
                insert i into m_t = [1]
                since we have processed k elements, our max in this window
                is at nums[m_t[0]] (2) , res = [2]
            2, 1, [2,1],[1],
                1 < nums[m_t[-1]](2), insert 2 into res = [2,2]
                insert i into m_t [1,2]
            3,0,[1,0],[1,2]
                m_t is not empty and m_t[0] is < i - k + 1
                pop_left from m_t, [2]
                0 < n[m_t[0]](1), insert 1 into res = [2,2,1]
                insert i into m_t [2,3]
            4,4,[0,4], [2,3]
                m_t is not empty and m_t[0](2) is < i(4) - k(2) + 1 = 3
                pop_left from m_t, [3]
                4 > n[m_t[0]] 3
        """