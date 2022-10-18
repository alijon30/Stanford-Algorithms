from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



def Traversal(root):
    result = []

    if not root:
        return result

    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        LeveLSize = len(queue)
        currentLevel = deque()

        for _ in range(LeveLSize):
            currentNode=  queue.popleft()

            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentNode.appendleft(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
                
        result.append(list(currentLevel))
        leftToRight = not leftToRight