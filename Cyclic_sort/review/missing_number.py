

def Solution(array):
    i, n = 0, len(array)

    while i < n:
        j = array[i]
        
        if i < n and array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1


    for i in range(len(array)):
        if array[i] != i:
            return i

    return n