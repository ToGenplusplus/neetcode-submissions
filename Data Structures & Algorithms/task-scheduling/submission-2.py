from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequency = Counter(tasks)
        max_heap = [-count for count in frequency.values()]
        heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                count = heappop(max_heap) + 1
                if count < 0:
                    q.append((time + n, count))

            if q and q[0][0] == time:
                entry = q.popleft()
                heappush(max_heap, entry[1])

        return time