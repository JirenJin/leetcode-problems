class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        history = set()
        while(True):
            if n not in history:
                history.add(n)
            else:
                return False
            square_sum = 0
            while(n > 0):
                square_sum += (n % 10) ** 2
                n /= 10
            if square_sum == 1:
                return True
            else:
                n = square_sum
