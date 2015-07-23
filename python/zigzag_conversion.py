class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s:
            return s
        new_s = ''
        for j in xrange(numRows):
            i = 0
            while(numRows*i + j < len(s)):
                new_s += s[numRows*i + j]
                i += 1
        return new_s.strip()
