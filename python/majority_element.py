class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        el_dict = dict()
        for n in nums:
            length = len(nums)
            if n not in el_dict:
                el_dict[n] = 1
            else:
                el_dict[n] += 1
            if el_dict[n] > length/2:
                return n
