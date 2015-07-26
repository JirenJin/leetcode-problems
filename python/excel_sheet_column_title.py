class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s = []
        while(n > 0):
            s.append((n - 1) % 26)
            n = (n - 1) / 26
        s = [chr(x + 65) for x in s]
        s = s[::-1]
        return ''.join(s)
