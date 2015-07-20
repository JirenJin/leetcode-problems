import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 1:
            return 0
        flag = [True] * n
        i = 2
        while(i*i < n):
            if not flag[i]:
                i += 1
                continue
            for j in xrange(i*i, n, i):
                flag[j] = False
            i += 1

        return sum(flag) - 2
