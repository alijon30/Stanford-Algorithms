
from heapq import *


class MedianOfStream:

    maxHeap = []
    minHeap = []

    def Insert(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)

        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


    def find_median(self):

        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2

        return self.maxHeap[0]/2