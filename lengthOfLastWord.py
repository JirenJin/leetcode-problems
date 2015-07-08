class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.split()
        if len(s) > 0:
            return len(s[-1])
        else:
            return 0
