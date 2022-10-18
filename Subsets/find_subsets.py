

def find_subsets(nums):

    subsets = []
    subsets.append([])

    for currentNums in nums:

        n = len(subsets)

        for i in range(n):
            subset1 = list(subsets[i])
            subset1.append(currentNums)
            subsets.append(subset1)

    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()