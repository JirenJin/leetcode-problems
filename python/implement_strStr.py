class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in xrange(len(haystack) - len(needle) + 1):
            for j in xrange(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
            else:
                return i
        else:
            return -1
