from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left, self.right = None, None



def Solution(root):
    queue = deque()
    queue.append(root)

    result = []

    while queue:
        levelLength = len(queue)

        for i in range(levelLength):
            currentNode = queue.popleft()

            if i == levelLength-1:
                result.append(currentNode)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = Solution(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()