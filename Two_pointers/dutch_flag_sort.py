

def dutch_flag_sort(array):
    low, high = 0, len(array) - 1
    i = 0

    while i <= high:
        if array[i] == 0:
            array[i], array[low]= array[low], array[i]

            i += 1
            low += 1
        elif array[i] == 1:
            i += 1

        else:
            array[i], array[high] = array[high], array[i]
            high -= 1