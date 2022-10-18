

def Solution(array1, array2):
    result = []

    i, j, start, end = 0,0,0 , 1

    while i < len(array1) and j < len(array2):
        a_overlaps_b = array1[i][start] >= array2[j][start] and array1[i][start] <= array2[j][end]

        b_overlaps_a = array2[j][start] >= array1[i][start] and array2[j][start] <= array1[i][end]

        if a_overlaps_b or b_overlaps_a:
            result.append([max(array1[i][start], array2[j][start], min(array1[i][end], array2[j][end]))])

        if array1[i][end] < array2[j][end]:
            i += 1
        else:
            j += 1

    return result