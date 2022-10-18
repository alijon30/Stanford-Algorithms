

def find_subarray(array, target):
    result = []
    left = 0
    product = 1

    for right in range(len(array)):
        product *= array[right]

        while product >= target and left < len(array):
            product /= array[left]
            left += 1

        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(array[i])
            result.append(list(temp_list))
    return result