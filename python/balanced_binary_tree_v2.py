# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.depth_of_node(root) != None

    def depth_of_node(self, node):
        if node == None:
            return 0
        else:
            l_depth = self.depth_of_node(node.left)
            if l_depth == None:
                return None
            r_depth = self.depth_of_node(node.right)
            if r_depth == None:
                return None
            if abs(l_depth - r_depth) > 1:
                self.result = False
                return None
            return max(l_depth, r_depth) + 1
