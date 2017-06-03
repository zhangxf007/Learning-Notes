class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if root is None:
            return None
        nodeA = self.traverse(root, A)
        nodeB = self.traverse(root, B)
        if nodeA is None or nodeB is None:
            return None

        hightA = self.hight(root, A)
        hightB = self.hight(root, B)

        # nodeTmp = TreeNode()
        if hightA > hightB:
            nodeTmp = nodeA
            nodeA = nodeB
            nodeb = nodeTmp

        nodeTmp = self.traverse(nodeA, nodeB)
        if nodeTmp:     # nodeB is the child of nodeA
            return nodeA

        # nodePar = TreeNode()
        nodePar = self.parentFind(root, nodeA)

        while nodePar:
             # if B is under nodePar, the nodeTmp will be the nodeB
             # otherwise return None
            nodeTmp = self.traverse(nodePar, nodeB)
            if nodeTmp:
                return nodePar
            else:
                nodePar = self.parentFind(root, nodePar)
        return None

    def traverse(self, node, target):
        # if target is in root tree, return the node reference in the tree
        # otherwise return None
        if node is None:
            return None
        if node.val == target.val:
            return node
        return self.traverse(node.left, target) or \
            self.traverse(node.right, target)


    def parentFind(self, node, target):
        # find the upper one level parent of target when node is the root
        # otherwise return None
        if node is None:
            return None
        if node.left == target or node.right == target:
            return node
        return self.parentFind(node.left, target) or \
            self.parentFind(node.right, target)

    def hight(self, root, target):
        # return the hight of target node in the root tree
        h1 = self.treeHeight(root)
        targetNode = self.traverse(root, target)
        h2 = self.treeHeight(targetNode)
        return h1 - h2 + 1

    def treeHeight(self, node):
        if node is None:
            return 0
        return max(self.treeHeight(node.left), self.treeHeight(node.right)) + 1


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    A = TreeNode(3)
    B = TreeNode(5)

    result = Solution().lowestCommonAncestor3(root, A, B)
    print result.val
