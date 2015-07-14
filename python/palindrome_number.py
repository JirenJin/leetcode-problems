class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        n = 0
        x_tmp = x
        while(x_tmp > 0):
            x_tmp /= 10
            n += 1
        while(n > 1):
            h = x / 10**(n-1)
            l = x - x/10*10
            if h != l:
                return False
            else:
                x = (x - h*10**(n-1) - l) / 10
                n -= 2
        else:
            return True
