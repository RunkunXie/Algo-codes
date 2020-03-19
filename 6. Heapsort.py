from typing import List
import heapq
from queue import PriorityQueue

class Solution:
    def heapSort(self, nums: List[int]) -> List[int]:
        a = []
        heapq.heapify(nums)

        for i in range(len(nums)):
            a.append(heapq.heappop(nums))
        return a


print(Solution().heapSort([5, 1, 1, 2, 0, 0]))


# maxHeapify, O(logn)
# buildMaxHeap, O(n) <- maxHeapify by n/2 times
# heapSort, O(nlogn)

# priority queue - O(logn):
# heapIncreaseKey, increase key and compare to its parent till the top
# maxHeapInsert, insert at bottom with k = -inf, then increase key
# heapExtractMax, pop top, remove bottom to the top, then heapify top
# heapMaximum, access top
