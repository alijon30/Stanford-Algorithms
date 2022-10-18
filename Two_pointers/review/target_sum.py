

def Solution(array, target):
    left, right = 0, len(array)-1

    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == target:
            return [left, right]

        elif currentSum > target:
            right -= 1
        else:
            left += 1


    return [-1, -1]

def main():
    print(Solution([1, 2, 3, 4, 6], 6))
    print(Solution([2, 5, 9, 11], 11))

main()