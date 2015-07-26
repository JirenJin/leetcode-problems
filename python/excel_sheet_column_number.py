class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        n = map(ord, s)
        n = [x - 64 for x in n]
        i = len(s) - 1
        num = 0
        for d in n:
            num += d * 26**(i)
            i -= 1
        return num
