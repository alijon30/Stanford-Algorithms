class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right=  None


def count_trees(num):
    if num <= 1:
        return 1
    count = 0

    for i in range(1, num+1):
        countOfLeft = count_trees(i-1)
        countOfRight = count_trees(num-i)

        count += countOfLeft * countOfRight

    return count

def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()