from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def Solution(root):
    if not root:
        return 0

    min_depth = 0

    queue = deque()
    queue.append(root)
    while queue:
        min_depth += 1
        LevelSize = len(queue)
        for _ in range(LevelSize):
            currentNode=  queue.popleft()

            if currentNode.left is None and currentNode.right is None:
                return min_depth

            if currentNode.left:
                queue.append(currentNode.val)

            if currentNode.right:
                queue.append(currentNode.right)