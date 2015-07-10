class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == None or n <= 0:
            return False
        if n == 1:
            return True
        divided = n / 2.0
        if divided == 1:
            return True
        elif divided != int(divided):
            return False
        else:
            return self.isPowerOfTwo(n/2)
