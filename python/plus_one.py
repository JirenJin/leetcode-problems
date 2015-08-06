class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        c = 1
        result = []
        for n in digits[::-1]:
            result.append((n + c) % 10)
            c = (n + c) / 10
        if c > 0:
            result.append(c)
        return result[::-1]
