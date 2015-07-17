class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums:
            return False
        value_dict = dict()
        for num in nums:
            if num not in value_dict:
                value_dict[num] = 1
            else:
                return True
        else:
            return False
