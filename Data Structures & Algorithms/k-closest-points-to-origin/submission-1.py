from heapq import heapify, heappush, heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        Input: points = [[0,2],[2,0],[2,2]], k = 2

        using a max heap

        i | points[i] | distance | operation | result
        0, [0,2], 4, add (-4,0,2) to heap | heap [(-4,0,2)]
        1, [2,0], 4, add (-4,2, 0) to heap | heap [(-4,0,2), (-4, 2, 0)]
        2, [2,2], 8, -8 < -4 , skip
        i, 3, loop is done

        return [[x,y] for dist,x,y in heap]

        max heap - numbers to add (-5,-2,-7)
        -5
        -5, -2
        -7, -5, -2
    
        """
        heap = []
        heapify(heap)

        for x, y in points:
            dist = -(x*x + y*y)

            if len(heap) < k:
                heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heappushpop(heap, (dist, x, y))

        return [[x,y] for (dist, x, y) in heap]
        