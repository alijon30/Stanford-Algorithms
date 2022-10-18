

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None



def count_paths(root, S):
    return count_paths_recursive(root, S, [])

def count_paths_recursive(root, S, currentPath):

    if root is None:
        return 0

    currentPath.append(root.value)
    pathCount, pathSum = 0, 0

    for i in range(len(currentPath)-1, -1,-1):
        pathSum += currentPath[i]
        if pathSum == S:
            pathCount += 1

    pathCount += count_paths_recursive(root.left, S, currentPath)
    pathCount += count_paths_recursive(root.right, S, currentPath)

    del currentPath[-1]
    return pathCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()