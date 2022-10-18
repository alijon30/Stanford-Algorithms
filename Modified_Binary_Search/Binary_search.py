

def Solution(array, target):

    start, end = 0, len(array)
    isAscending = array[start] < array[end]
    while start <= end:
        middle = start +  (end - start)//2

        if target == array[middle]:
            return middle

        if isAscending:
            if target > array[middle]:
                start = middle + 1
            else:
                end = middle - 1
        else:
            if target < array[middle]:
                start = middle + 1
            else:
                end = middle - 1

