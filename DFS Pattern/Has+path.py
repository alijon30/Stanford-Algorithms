class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left, self.right = left, right


def has_path(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum-root.val)
