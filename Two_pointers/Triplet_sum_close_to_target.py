import math

def triplet_sum_close_to_target(array, target_sum):
    array.sort()
    smallest_difference = math.inf

    for i in range(len(array)-2):
        left = i + 1
        right = len(array)-1

        while left < right:
            target_diff = target_sum - array[i] - array[left] - array[right]

            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest