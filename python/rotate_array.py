class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if nums:
            while(k > 0):
                nums[0:0] = [nums.pop(-1)]
                k -= 1
