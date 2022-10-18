

def Solution(array, target):
    array.sort()
    count = 0
    for i in range(len(array)-2):
        count += search_pair(array, target - array[i], i)

    return count


def search_pair(array, target_Sum, first):
    left = first + 1
    right = len(array) - 1
    count = 0

    while left < right:
        if array[left] + array[right] < target_Sum:
            count += 1
            left += 1

        else:
            right -= 1

    return count