

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None



def find_path(root, sequence):
    return find_path_recursive(root, sequence, 0)

def find_path_recursive(root, sequence, sequenceIndex):
    if root is None:
        return False

    seqLen = len(sequence)

    if sequenceIndex >= seqLen or root.value != sequence[sequenceIndex]:
        return False

    if root.left is None and root.right is None and sequenceIndex == seqLen-1:
        return True

    return find_path_recursive(root.left, sequence, sequenceIndex+1) or find_path_recursive(root.right, sequence, sequenceIndex+1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()