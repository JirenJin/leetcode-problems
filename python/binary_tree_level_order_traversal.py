# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return []
        current = [root]
        all_layers = []
        while(current):
            all_layers.append([node.val for node in current])
            current = [n for node in current for n in (node.left, node.right) if n]
        return all_layers

binary_tree_level_order_traversal
