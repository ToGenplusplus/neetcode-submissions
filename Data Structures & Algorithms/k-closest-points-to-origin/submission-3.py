from heapq import heapify, heappush, heappushpop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        heapify(max_heap)

        for x, y in points:

            dist = - (x*x + y*y)

            if len(max_heap) < k:
                heappush(max_heap, (dist, x, y))
            elif dist > max_heap[0][0]:
                heappushpop(max_heap, (dist, x, y))

        return [[x,y] for (dist, x, y) in max_heap]


        """
            points=[[-5,4],[-6,-5],[4,6]]
            k=2

            i | points[i] | dist |
            0 | [-5,4] | 41 | add to heap [-41]
            1 | [-6, -5], 61 | add to heap [-61, -41]
            2 | [4, 6] | 52, add to heap remove min [-52, -41]
        """




        