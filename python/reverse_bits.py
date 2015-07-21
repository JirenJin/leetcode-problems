class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = []
        while(n > 0):
            s.append(n % 2)
            n /= 2
        reverse = 0
        i = 31
        while(s):
            reverse += 2**i * s.pop(0)
            i -= 1
        return reverse
