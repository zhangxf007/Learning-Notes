# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
#
# A valid path is from root node to any of the leaf nodes.

# Example
# Given a binary tree, and target = 5:
#
#      1
#     / \
#    2   4
#   / \
#  2   3
# return
#
# [
#   [1, 2, 2],
#   [1, 4]
# ]



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths


    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, result, [], target)
        return result

    def dfs(self, node, result, tmp, target):
        tmp.append(node.val)
        if node.left is None and node.right is None:
            if target == sum(tmp):
                #print tmp
                result.append(tmp[:])
            tmp.pop()
            return

        if node.left:
            self.dfs(node.left, result, tmp, target)
        if node.right:
            self.dfs(node.right, result, tmp, target)
        tmp.pop()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(4)
    result = Solution().binaryTreePathSum(root, 5)
    print result
