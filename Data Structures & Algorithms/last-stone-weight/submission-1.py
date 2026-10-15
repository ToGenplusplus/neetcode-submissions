from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapify(heap)

        while len(heap) > 1:
            y,x = heappop(heap), heappop(heap)

            if x != y:
                heappush(heap, y - x)

        return -heap[0] if heap else 0
        """
            use a max heap (- input values)

            iterate through heap while there are at least 2 elements

                pop the two biggest stones

                if they are not equal

                    add the difference of the bigger - smaller into heap

            return heap[0] is len(heap) else 0

        """        

