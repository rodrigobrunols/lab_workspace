class TreeNode:
    def __init__(self, value:int, left=None, right=None):
        self.val = value
        self.right = right
        self.left = left


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> [int]:

        def is_leaf(node):
            return node and not node.left and not node.right

        def get_left_bound(node):
            while node:
                if not is_leaf(node):
                    result.append(node.val)

                node = node.left if node.left else node.right


        def get_leafs(node):
            if node:
                if is_leaf(node):
                    result.append(node.val)
                else:
                    get_leafs(node.left)
                    get_leafs(node.right)


        def get_right_bound(node):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)

                node = node.right if node.right else node.left

            while stack:
                result.append(stack.pop())

        result = []
        if not root:
            return result

        result.append(root.val)

        get_left_bound(root.left)
        get_leafs(root)
        get_right_bound(root.right)


        return result



if __name__ == "__main__":
    # Construct the binary tree for Example 1:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #        \
    #         7
    node7 = TreeNode(7)
    node5 = TreeNode(5, None, node7)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node4, node5)
    node6 = TreeNode(6)
    node3 = TreeNode(3, None, node6)
    root = TreeNode(1, node2, node3)

    sol = Solution()
    boundary = sol.boundaryOfBinaryTree(root)
    print("Boundary of Binary Tree:", boundary)





