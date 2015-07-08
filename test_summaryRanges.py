import unittest

from summaryRanges import Solution

class summaryRangesTests(unittest.TestCase):

    def test_continuous_nums(self):
        nums = [0,1,2,3]
        s = Solution()
        result = s.summaryRanges(nums)
        self.failUnless(result == ["0->3"])
    def test_two_parts_continuous_nums(self):
        nums = [-2147483648, -2147483647, 2147483647]
        s = Solution()
        result = s.summaryRanges(nums)
        print nums, result
        self.failUnless(result == ["-2147483648->-2147483647", "2147483647"])
    def test_single_number_nums(self):
        nums = [0,1,4,7,8,10]
        s = Solution()
        result = s.summaryRanges(nums)
        print nums, result
        self.failUnless(result == ["0->1", "4", "7->8", "10"])
    def test_null_nums(self):
        nums = []
        s = Solution()
        result = s.summaryRanges(nums)
        self.failUnless(result == [])


if __name__ == "__main__":
    unittest.main()
