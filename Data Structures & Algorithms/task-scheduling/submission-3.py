from collections import deque, Counter
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            tasks = ["X","X","Y","Y","Z"], n = 2
            X,Y,Z,X,Y,.,X
            x -> 3
            y -> 2
            z -> 1

            time, task, remainder
            1, X -> x:2
            2,Y -> y:1
            3,Z z:0
            4,X x:1
            5 y: y0
            6
                only 1 task remianing x
                last x ran at time 4
                currtime - past time = 2 = n, cant run
            7,
                only 1 task remianing x
                last x ran at time 4
                7 -4 = 3 > 2 - run X

            min -> 7


            approach
                get the frequency of each task in tasks
                insert frequencies into max heap
                iterate through the heap
                    increase time
                    pop the max value
                        add + 1
                        if >= 0 do nothing else
                        add value,time + n to queue

                    check if process_time at top of q is == curr_time
                        if so remove from q
                        add to max_heap
        """

        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapify(max_heap)

        q = deque()

        time = 0

        while max_heap or q:
            time += 1
            
            if max_heap:
                count = heappop(max_heap) + 1
                if count < 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heappush(max_heap, q.popleft()[0])

        return time

        """
            ["X","X","Y","Y"], n = 2
            x:3
            y:2
            heap = [-3,-2]


            time, 
            1, -3 + 1 = -2 < 0, q = [(-2, 3)]
            2, -2 + 1 = -1 < 0, q = [(-2, 3), (-1, 4)]
            3
                pop (-2,3) from q, add -2 to heap [-2]
            4, [-2]
                -2 + 1 = -1 < 0, add (-1, 6) to q
                q[0][1] = 4 = time
                    popleft (-1,4) from q, add (-1) to heap [-1]
            5, [-1], q= [(-1,6)]
                -1 + 1 = 0
                q[0][1] = 6 > 5
            6
                q[0][1] = 6 = time
                    popleft (-1,6) from q, add (-1) to heap [-1], q = []

            7, [-1], []
                -1 + 1 = 0 



        """

