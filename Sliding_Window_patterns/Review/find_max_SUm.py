

def find_Max_Sub_array(arr, k):
    window_start = 0
    window_Sum = 0
    max_Sum = 0

    for window_end in range(len(arr)):
        window_Sum += arr[window_end]

        if window_end >= k-1:
            max_Sum = max(max_Sum, window_Sum)
            window_Sum -= arr[window_start]
            window_start += 1

    return max_Sum