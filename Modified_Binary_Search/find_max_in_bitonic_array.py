

def find_max_in_bitonic_array(array):
    start, end = 0, len(array)-1

    while start < end:
        middle = start + (end-start)//2

        if array[middle] > array[middle + 1]:
            end = middle
        else:
            start = middle + 1

    return array[start]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()