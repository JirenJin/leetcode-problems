# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        depth = 0
        if root:
            depth = 1
        else:
            return 0
        current_layer = [root]
        while(True):
            next_layer = []
            for node in current_layer:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            current_layer = next_layer
            depth += 1


