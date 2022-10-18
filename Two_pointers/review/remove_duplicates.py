

def Solution(array):
    next_non_duplicate = 1
    i = 0

    while i < len(array):
        if array[next_non_duplicate-1] != array[i]:
            array[next_non_duplicate]= array[i]
            next_non_duplicate += 1

        i += 1

    return next_non_duplicate


def main():
    print(Solution([2, 3, 3, 3, 6, 9, 9]))
    print(Solution([2, 2, 2, 11]))

main()