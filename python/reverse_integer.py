class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        string = str(abs(x))
        r = sign * int(string[::-1])
        return 0 if abs(r) > 2**31 else r
