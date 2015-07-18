class BST:
    def __init__(self, index, val):
        self.val = val
        self.index = index
        self.left = None
        self.right = None




class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def __init__(self):
        self.is_duplicated = False


    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False
        if k < 0 or t < 0:
            return False
        for i, num in enumerate(nums):
            if i == 0:
                root = BST(0, nums[0])
            else:
                node = BST(i, num)
                self.insert_node(root, node, k, t)
                if self.is_duplicated == True:
                    return True
        else:
            return False


    def insert_node(self, root, node, k, t):
        if (abs(node.val - root.val) <= t) and abs(node.index - root.index) <= k:
            self.is_duplicated = True
        else:
            if node.val < root.val:
                if root.left:
                    self.insert_node(root.left, node, k, t)
                else:
                    root.left = node
            elif node.val > root.val:
                if root.right:
                    self.insert_node(root.right, node, k, t)
                else:
                    root.right = node
            else:
                root.index = node.index
                root.val = node.val




