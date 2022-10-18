import math


def Solution(arr, S):
    window_start = 0
    window_Sum = 0
    max_length = math.inf

    for window_end in range(len(arr)):
        window_Sum += arr[window_end]

        while window_Sum >= S:
            window_Sum -= arr[window_start]
            window_start += 1

        max_length = min(max_length, window_end - window_start + 1)