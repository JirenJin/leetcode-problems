class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        s = []
        while(n > 0):
            s.append(n % 2)
            n /= 2
        return sum(s)
