from collections import Counter, deque
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapify(max_heap)

        q = deque([])

        time = 0
        while max_heap or q:
            time += 1
            if len(max_heap) > 0:
                count = heappop(max_heap)
                count += 1
                if count < 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                entry = q.popleft()
                heappush(max_heap, entry[0])

        return time

        """
            tasks = ["X","X","Y","Y"], n = 2
            X -> 2
            Y -> 2

            max_heap = [-2, -2]

            q = deque([])

            time | max_heap | q | operation | result
            1 | -2 | [] | -2 + 1 = -1 < 0, add (-1, time + n) to q
            2 | -2 | [(-1, time + n)], -2 + 1 = -1 < 0, add (-1, time + n) to q
                q is not empty, q[0][0] > current time, nothing to process continues
            3 | [], [(-1, 3), (-1, 4)], 
                heap is empty but queue is not empty
                q[0][0] == current_time
                popleft entry from q, add entry[0] to heap
            4 | [-1], 
                heap is not emtpy

        """
