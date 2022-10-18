class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, required_Sum):
    allPaths = []
    find_paths_recursive(root, required_Sum, [], allPaths)
    return allPaths

def find_paths_recursive(currentNode, required_Sum, currentPath, allPaths):
    if currentNode is None:
        return

    currentPath.append(currentNode.val)

    if currentNode.val == required_Sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(currentPath)

    else:
        find_paths_recursive(currentNode.left, required_Sum, currentPath, allPaths)

        find_paths_recursive(currentNode.right, required_Sum, currentPath, allPaths)

    del currentPath[-1]