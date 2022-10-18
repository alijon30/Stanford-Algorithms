
from collections import deque

def find_permutations(nums):
    nums_length = len(nums)
    Permutations = deque()
    Permutations.append([])
    result = []
    for currentNum in nums:

        n = len(Permutations)

        for _ in range(n):
            oldPermutation = Permutations.popleft()

            for j in range(len(oldPermutation) + 1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNum)

                if len(newPermutation) == nums_length:
                    result.append(newPermutation)
                else:
                    Permutations.append(newPermutation)

    return result

def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result

def generate_permutations_recursive(nums, currentIndex, currentPermutation, result):
    if len(currentPermutation) == len(nums):
        result.append(currentPermutation)

    else:
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[currentIndex])
            generate_permutations_recursive(nums, currentIndex + 1, newPermutation, result)