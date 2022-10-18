from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def Solution(root):
    result = []
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []

        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        result.append(currentLevel)