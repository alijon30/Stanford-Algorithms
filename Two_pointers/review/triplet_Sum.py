

def Solution(array):
    array.sort()
    triplets = []

    for i in range(len(array)):
        if i > 0 and array[i] == array[i-1]:
            continue
        find_pairs(array, -array[i], i+1, triplets)

    return triplets

def find_pairs(array, targetSum, left, triplets):
    right = len(array) -1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            triplets.append([-targetSum, array[left], array[right]])
            left += 1
            right -= 1

            while left < right and array[left] == array[left-1]:
                left += 1
            while left < right and array[right] == array[right+1]:
                right -= 1
        elif currentSum > targetSum:
            right -= 1
        else:
            left += 1

def main():
  print(Solution([-3, 0, 1, 2, -1, 1, -2]))
  print(Solution([-5, 2, -1, -2, 3]))


main()