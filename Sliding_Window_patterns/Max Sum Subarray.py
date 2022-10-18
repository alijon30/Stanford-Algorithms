

class Solution:
    def MaxSumSubarray(self, array, k):
        max_Sum = 0
        window_start = 0
        window_Sum = 0

        for window_end in range(len(array)):
            window_Sum += array[window_end]

            if window_end >= k -1:
                max_Sum = max(max_Sum, window_Sum)
                window_Sum -= array[window_start]
                window_start +=1

        return max_Sum









array = [2, 1, 5, 1, 3, 2]
k=7
Output = 9

solution = Solution()
print(solution.MaxSumSubarray(array, k))