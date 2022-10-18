from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left, self.right, self.next = None, None, None

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def Solution(root):
    queue = deque()

    queue.append(root)
    currentNode, previousNode = None, None
    while queue:

        currentNode = queue.popleft()

        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        if currentNode.left:
            queue.append(currentNode.left)

        if currentNode.right:
            queue.append(currentNode.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  Solution(root)
  root.print_tree()


main()