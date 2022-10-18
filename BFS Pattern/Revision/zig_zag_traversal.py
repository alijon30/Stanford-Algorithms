from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def Solution(root):
    queue = deque()
    queue.append(root)
    result = []
    Left_To_Right = True
    while queue:
        currentLevel = deque()
        currentLength = len(queue)

        for _ in range(currentLength):
            currentNode = queue.popleft()

            if Left_To_Right:
                currentLevel.append(currentNode.value)
            else:
                currentLevel.appendleft(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)

            if currentNode.right is not None:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
        Left_To_Right = not Left_To_Right


    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(Solution(root)))


main()

