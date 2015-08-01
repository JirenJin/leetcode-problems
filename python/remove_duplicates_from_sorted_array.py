class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        while(i < len(nums)-1):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
