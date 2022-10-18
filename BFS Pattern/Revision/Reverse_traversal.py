from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right=  None, None



def Solution(root):
    result = deque()
    queue = deque()
    queue.append(root)

    while queue:
        currentLevel = []
        LevelLength= len(queue)

        for _ in range(LevelLength):
            rootNode = queue.popleft()

            currentLevel.append(rootNode.value)

            if rootNode.left is not None:
                queue.append(rootNode.left)

            if rootNode.right is not None:
                queue.append(rootNode.right)

        result.appendleft(currentLevel)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(list(Solution(root))))


main()