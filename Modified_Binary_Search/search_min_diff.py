

def Solution(array, key):
    if key < array[0]:
        return array[0]
    elif key > array[-1]:
        return array[-1]

    start, end = 0, len(array)-1

    while start <= end:
        middle = start + (end-start)//2

        if key < array[middle]:
            end = middle - 1
        elif key > array[middle]:
            start =  middle + 1
        else:
            return array[middle]


    if (array[start]-key) < (key - array[end]):
        return array[start]
    return array[end]