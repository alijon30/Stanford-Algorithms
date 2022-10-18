def removeDuplicates(array):
    next_non_duplicate = 1

    i = 0
    while i < len(array):
        if array[next_non_duplicate - 1] != array[i]:
            array[next_non_duplicate] = array[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate
