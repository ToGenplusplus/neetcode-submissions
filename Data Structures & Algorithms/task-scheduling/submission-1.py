from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            tasks = ["A","A","A","B","C"], n = 3

            A -> 3
            B -> 1
            C -> 1

            place the counts in a max_heap (negated min heap)

            -3, -1 -1

            time | heap[0] | q[0] | operation(s) | result
            1, -3, none, -3 + 1, insert (-2, 4) into q
            2, -1, (-2,4), -1 + 1 = 0, 2 != 4 - nothing to do
            3, -1, (-2,4), -1 + 1, = 0
        """
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapify(max_heap)

        cool_down = deque([])
        time = 0

        while max_heap or cool_down:
            time +=1
            if max_heap:
                count = heappop(max_heap) + 1
                if count < 0:
                    cool_down.append((count, time + n))

            if cool_down and time == cool_down[0][1]:
                heappush(max_heap, cool_down.popleft()[0])

        return time
