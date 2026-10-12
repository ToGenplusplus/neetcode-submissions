from heapq import heapify, heappop, heappush
#readable solution

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)

        while len(heap) > 1:
            i = heappop(heap)
            j = heappop(heap)

            if i != j:
                heappush(heap, i - j)

        return - heap[0] if heap else 0

        