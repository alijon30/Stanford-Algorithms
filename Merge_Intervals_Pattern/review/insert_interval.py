

def Solution(array, new_interval):
    merged = []

    i, start, end = 0, 0, 1


    while i < len(array) and array[i][start] < new_interval[end]:
        merged.append(array[i])
        i += 1

    while i < len(array) and array[i][start] <= new_interval[end]:
        new_interval[start] = min(array[i][start], new_interval[start])
        new_interval[end] = max(array[i][end], new_interval[end])
        i += 1

    merged.append(new_interval)

    while i < len(array):
        merged.append(array[i])
        i += 1
    return merged