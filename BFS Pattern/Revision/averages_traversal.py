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
        currentVal = 0
        current_length=  len(queue)

        for _ in range(current_length):
            rootNode = queue.popleft()

            currentVal += rootNode.value

            if rootNode.left is not None:
                queue.append(rootNode.left)

            if rootNode.right is not None:
                queue.append(rootNode.right)

        result.append(currentVal/current_length)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(Solution(root)))


main()