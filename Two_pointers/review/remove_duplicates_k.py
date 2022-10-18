

def Solution(array, key):
    nextNonDuplicate = 0

    for i in range(len(array)):
        if array[i] != key:
            array[nextNonDuplicate] = array[i]
            nextNonDuplicate += 1

    return nextNonDuplicate