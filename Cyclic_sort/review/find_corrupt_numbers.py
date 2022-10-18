

def Solution(array):

    i = 0

    while i < len(array):
        j = array[i] - 1

        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]

        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            return [array[i], i + 1]

    return [-1, -1]

def main():
    print(Solution([3, 1, 2, 5, 2]))
    print(Solution([3, 1, 2, 3, 6, 4]))

main()