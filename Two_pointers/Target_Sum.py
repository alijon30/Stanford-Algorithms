

def target_Sum(array, target):
    left, right = 0, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target:
            return [left, right]

        if current_sum > target:
            right -= 1

        else:
            left += 1

    return [-1, -1]

def Target_Sum(array, target):
    nums = {}

    for i, num in enumerate(array):
        if target - num in nums:
            return [nums[target-num], i]
        else:
            nums[num] = i

    return [-1, -1]