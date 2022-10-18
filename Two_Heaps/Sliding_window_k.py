from heapq import *
import heapq



class SlidingWindowMedian:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def find_sliding_window_median(self, nums, k):
        res = [0.0 for x in range(len(nums)-k+1)]

        for i in range(0, len(nums)):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:

                if len(self.maxHeap) == len(self.minHeap):
                    res[i-k+1] = -self.maxHeap[0]/2 + self.minHeap[0]/2
                else:
                    res[i-k+1] = -self.maxHeap[0]/2

                element_to_be_removed = nums[i-k+1]
                if element_to_be_removed <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -element_to_be_removed)
                else:
                    self.remove(self.minHeap, element_to_be_removed)

                self.rebalance_heaps()
        return res

    def remove(self, heap, element):
        ind = heap.index(element)

        heap[ind] = heap[-1]
        del heap[-1]

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))



def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))


main()