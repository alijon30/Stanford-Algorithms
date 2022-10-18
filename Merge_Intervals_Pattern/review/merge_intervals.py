class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge_intervals(array):

    array.sort(key = lambda x: x.start)
    merged_array = []
    start =array[0].start
    end = array[0].end

    for i in range(1, len(array)):
        if array[i].start <= end:
            end = max(end, array[i].end)
        else:
            merged_array.append(Interval(start, end))
            start = array[i].start
            end = array[i].end

    merged_array.append(Interval(start, end))
    return merged_array

def main():
    print("Merged intervals: ", end='')
    for i in merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

main()