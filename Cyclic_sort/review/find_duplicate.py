


def Solution(array):
    i = 0

    while i < len(array):

        if array[i] != i + 1:
            j = array[i] - 1

            if array[i] != array[j]:
                array[i], array[j] = array[j] = array[i]

            else:
                return array[i]
        else:
            i += 1