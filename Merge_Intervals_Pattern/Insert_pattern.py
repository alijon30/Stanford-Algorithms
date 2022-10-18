


def insert(intervals, new_interval):
    merged = []

    i, start, end = 0, 0, 1


    #merge all intervals that come before new_interval
    while i < len(intervals) and intervals[i][end] < intervals[i][start]:
        merged.append(intervals[i])
        i += 1

    #merge all intervals that overlap with new_interval

    while i < len(intervals) and intervals[i][start] <= intervals[i][end]:
        new_interval[start] = min(intervals[i][start], intervals[start])
        new_interval[end] = max(intervals[i][start])
        i +=1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged
    