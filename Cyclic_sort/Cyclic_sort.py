def Sort(array):
    i = 0

    while i < len(array):
        j = array[i] - 1

        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]

        else:
            i += 1