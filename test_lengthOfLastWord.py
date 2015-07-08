import unittest
from lengthOfLastWord import Solution

class TestLengthOfLastWord(unittest.TestCase):

    def test_single_word(self):
        result = Solution()
        s = 'hello'
        length = result.lengthOfLastWord(s)
        self.failUnless(length == 5)

    def test_double_word(self):
        result = Solution()
        s = 'hello world'
        length = result.lengthOfLastWord(s)
        self.failUnless(length == 5)

    def test_last_space(self):
        result = Solution()
        s = 'hello '
        length = result.lengthOfLastWord(s)
        self.failUnless(length == 5)

    def test_single_space(self):
        result = Solution()
        s = ' '
        length = result.lengthOfLastWord(s)
        self.failUnless(length == 0)

    def test_double_space(self):
        result = Solution()
        s = '  '
        length = result.lengthOfLastWord(s)
        self.failUnless(length == 0)


if __name__ == '__main__':
    unittest.main()
