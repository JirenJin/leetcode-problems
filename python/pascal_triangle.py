class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        rows_list = []
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 1:
            return [[1], [1,1]]
        rows_list.append([1])
        rows_list.append([1,1])
        for i in xrange(2, numRows):
            row = []
            for j in xrange(0, len(rows_list[i-1]) - 1):
                row.append(rows_list[i-1][j] + rows_list[i-1][j+1])
            rows_list.append([1] + row + [1])
        return rows_list
