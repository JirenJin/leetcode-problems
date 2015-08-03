class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums:
            return
        i = 0
        while(i < len(nums)):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
