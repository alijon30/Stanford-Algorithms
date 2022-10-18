

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None



def path_Sum(root):
    return path_Sum_recursive(root, 0)

def path_Sum_recursive(root, pathSum):

    if root is None:
        return 0

    pathSum += 10 * pathSum + root.value

    if root.left is None and root.right is None:
        return pathSum

    return path_Sum_recursive(root.left, pathSum) + path_Sum_recursive(root.right, pathSum)


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(path_Sum(root)))


main()