class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        row = []
        for i in xrange(rowIndex + 1):
            row.append(self.cnk(rowIndex, i))
        return row

    def cnk(self, n, k):
        r = 1
        for i in xrange(n, n-k, -1):
            r *= i
        for j in xrange(1, k+1):
            r /= j
        return r
