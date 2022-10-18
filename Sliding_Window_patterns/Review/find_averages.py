

def find_averages(array, k):
    result = []

    window_Sum, window_start = 0,0

    for window_end in range(len(array)):
        window_Sum += array[window_end]

        if window_end >= k -1:
            result.append(window_Sum/k)
            window_Sum -= array[window_start]
            window_start += 1

    return result


def main():
    print("Averages of subarrays of size K : " + str(find_averages([1, 3, 2, 6, -1, 4, 1, 8 , 2], 5)))

main()