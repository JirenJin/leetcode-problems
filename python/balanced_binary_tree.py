# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.result = True
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        self.result = True
        self.depth_of_node(root)
        return self.result

    def depth_of_node(self, node):
        if node == None:
            return 0
        else:
            l_depth = self.depth_of_node(node.left)
            if l_depth == -1:
                return -1
            r_depth = self.depth_of_node(node.right)
            if r_depth == -1:
                return -1
            if abs(l_depth - r_depth) > 1:
                self.result = False
                return -1
            return max(l_depth, r_depth) + 1



