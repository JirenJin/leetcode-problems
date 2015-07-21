class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        pre = 0
        current = 0
        for n in nums:
            tmp = max(pre + n, current)
            pre = current
            current = tmp
        return current
