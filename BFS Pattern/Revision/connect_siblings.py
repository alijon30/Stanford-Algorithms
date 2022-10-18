from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

def connect_Siblings(root):
    queue = deque()
    queue.append(root)

    while  queue:
        previousNode = None
        levelSize = len(queue)

        for _ in range(levelSize):
            rootNode = queue.popleft()

            if previousNode:
                previousNode.next = rootNode
            previousNode = rootNode

            if rootNode.left:
                queue.append(rootNode.left)

            if rootNode.right:
                queue.append(rootNode.right)



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_Siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()

