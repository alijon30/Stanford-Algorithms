import math
class Solution:
    def SmallestSumSubarray(self, array, limit):
        min_length = math.inf
        window_start = 0
        window_Sum = 0


        for window_end in range(len(array)):
            window_start += array[window_end]

            while window_Sum >= limit -1:
                min_length = min(min_length, window_end - window_start + 1)
                window_Sum -= array[window_start]
                window_start += 1

        return min_length








array = [17,85,93,-45,-21]
k = 150

solution = Solution()
print(solution.SmallestSumSubarray(array, k))