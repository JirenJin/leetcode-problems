class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if len(nums) > 0:
            start = nums[0]
            if len(nums) == 1:
                return [str(start)]
            for i in xrange(1, len(nums)):
                pre = nums[i - 1]
                current = nums[i]
                if current != pre + 1:
                    if start == pre:
                        ranges.append(str(start))
                    else:
                        ranges.append(str(start) + '->' + str(pre))
                    start = current
                    if i == len(nums) - 1:
                        ranges.append(str(start))
                else:
                    if i == len(nums) - 1:
                        ranges.append(str(start) + '->' + str(current))
                    continue
        return ranges
