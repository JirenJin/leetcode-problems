class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root:
            left_depth =  self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        else:
            return 0
