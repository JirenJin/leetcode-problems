# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = []
        s = 0
        stack.append((root, 0))
        while(stack):
            node, s = stack.pop(-1)
            s += node.val
            if node.left:
                stack.append((node.left, s))
            if node.right:
                stack.append((node.right, s))
            if not node.left and not node.right:
                if s == sum:
                    return True
        return False

