

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def find_unique_trees(num):
    if num <= 0:
        return []
    return find_unique_trees_recursive(1, num)


def find_unique_trees_recursive(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end+1):
        leftSubtrees = find_unique_trees_recursive(start, i-1)
        rightSubtress = find_unique_trees_recursive(start+1, i)

        for leftTree in leftSubtrees:
            for rightTree in rightSubtress:
                root = TreeNode(i)
                root.left = leftTree
                root.right = rightTree
                result.append(root)

    return result

def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()