class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False
        if k <= 0:
            return False
        value_dict = dict()
        for i, num in enumerate(nums):
            if num not in value_dict:
                value_dict[num] = i
            else:
                if i - value_dict[num] <= k:
                    return True
                else:
                    value_dict[num] = i
        else:
            return False
