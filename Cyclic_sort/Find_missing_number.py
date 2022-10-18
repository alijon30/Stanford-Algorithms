

def find_missing_numer(nums):
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1


    for i in range(n):
        if nums[i] != i:
            return i