from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None



def Solution(root):
    queue = deque()
    queue.append(root)
    min_length = 0

    while queue:
        min_length += 1
        levelSize = len(queue)

        for _ in range(levelSize):
            rootNode=  queue.popleft()

            if not rootNode.left and not rootNode.right:
                return min_length

            if rootNode.left is not None:
                queue.append(rootNode.left)

            if rootNode.right is not None:
                queue.append(rootNode.right)

    return min_length

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(Solution(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(Solution(root)))


main()