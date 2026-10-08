from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        

    def add(self, val: int) -> int:

        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            # Pushes val and pops the root in a single efficient operation
            heappushpop(self.minHeap, val)

        return self.minHeap[0]
        
