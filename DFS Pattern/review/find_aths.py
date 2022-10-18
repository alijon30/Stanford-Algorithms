
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None



def find_paths(root, Sum):
    allpaths = []
    find_paths_recursive(root, Sum, [], allpaths)
    return allpaths

def find_paths_recursive(root, currentSum, currentPath, allpaths):
    if root is None:
        return

    currentPath.append(root.value)

    if root.value == currentSum and root.left is None and root.right is None:
        allpaths.append(list(currentPath))
    else:
        find_paths_recursive(root.left, currentSum - root.value, currentPath, allpaths)
        find_paths_recursive(root.right, currentSum-root.value, currentPath, allpaths)

    del currentPath[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()