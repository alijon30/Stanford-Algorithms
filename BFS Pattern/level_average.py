from collections import  deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right=  None, None


def Solution(root):
    result = []

    if not root:
        return root

    queue = deque()
    queue.append(root)

    while queue:
        LeveLSize = len(queue)
        LevelSum = 0

        for _ in range(LeveLSize):
            currentNode = queue.popleft()
            LevelSum += currentNode.val

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        result.append(LevelSum/LeveLSize)
        