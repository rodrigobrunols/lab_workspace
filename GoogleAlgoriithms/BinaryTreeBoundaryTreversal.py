class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None


def traversal(root: TreeNode) -> list:
    if not root:
        return []

    result = []
    visited = set()

    def left_side(node):
        current = node
        while current:
            if current not in visited:
                result.append(current.val)
                visited.add(current)
                current = current.left

    def is_leaf(node):
        return node is not None and node.left is None and node.right is None

    def bottom(node):
        if node:
            if is_leaf(node) and node not in visited:
                result.append(node.val)
                visited.add(node)
            else:
                bottom(node.left)
                bottom(node.right)

    def right_side(node):
        current = node.right
        stack = []
        while current and current not in visited:
            stack.append(current.val)
            visited.add(current)
            current = current.right

        # print(stack)
        while stack:
            result.append(stack.pop())

    left_side(root)
    bottom(root)
    right_side(root)

    return result


node2 = TreeNode(2)
node2.left = TreeNode(4)

node5 = TreeNode(5)
node5.left = TreeNode(8)
node5.right = TreeNode(9)
node2.right = node5


node3 = TreeNode(3)
node3.left = TreeNode(6)
node3.right = TreeNode(7)

root = TreeNode(1)
root.left = node2
root.right = node3

print(traversal(root))


