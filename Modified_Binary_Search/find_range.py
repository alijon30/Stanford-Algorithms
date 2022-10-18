
def find_range(array, key):
    result = [-1, -1]
    result[0] = binary_search(array, key, False)

    if result[0] != -1:
        result[-1] = binary_search(array, key, True)

    return result

def binary_search(array, key, findMaxIndex):
    keyIndex = -1

    start, end = 0, len(array)-1

    while start <= end:
        middle = start + (end - start)//2

        if key < array[middle]:
            end = middle - 1
        elif key > array[middle]:
            start = middle + 1
        else:
            keyIndex = middle
            if findMaxIndex:
                start = middle + 1
            else:
                end = middle - 1
    return keyIndex