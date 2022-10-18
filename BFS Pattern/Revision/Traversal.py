from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None




def Solution(root):
    queue = deque()
    queue.append(root)
    result = []

    while queue:
        currentLevel = []
        LevelLength = len(queue)

        for _ in range(LevelLength):
            currentNode= queue.popleft()

            currentLevel.append(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)

            if currentNode.right is not None:
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(Solution(root)))


main()