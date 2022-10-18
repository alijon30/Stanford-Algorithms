
def make_squares(array):
    new_res = [0 for i in range(len(array))]
    highest_index= len(array) - 1
    left, right = 0, len(array)- 1

    while left < right:
        leftSquare = array[left] * array[left]
        rightSquare = array[right] * array[right]

        if leftSquare > rightSquare:
            new_res[highest_index] = leftSquare
            left += 1

        else:
            new_res[highest_index] = rightSquare
            right -= 1

        highest_index -= 1