from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right=  None, None


def Solution(root, key):
    if not root:
        return 0

    queue = deque()
    queue.append(root)

    while queue:
        currentNode= queue.popleft()

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        if currentNode.val == key:
            break

    return queue[0] if queue else None