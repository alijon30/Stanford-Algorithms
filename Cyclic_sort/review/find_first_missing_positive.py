

def Solution(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j] , nums[i]


    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

        