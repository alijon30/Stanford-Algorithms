

def Solution(array):
    array.sort()
    left, right = 0, len(array)-1
    highest_Index = len(array)-1

    while left < right:
        leftProduct = array[left] * array[left]
        RightProduct = array[right] * array[right]

        if leftProduct <= RightProduct:
            array[highest_Index] = RightProduct
            highest_Index -= 1
            left
        else:
            array[highest_Index] = leftProduct
            highest_Index -= 1
