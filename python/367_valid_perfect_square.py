class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        start = 1
        end = num
        half = (end - start) / 2
        while half > 0:
            pivot = start + half
            if pivot ** 2 == num:
                return True
            elif pivot ** 2 < num:
                start = pivot
            else:
                end = pivot
            half = (end - start) / 2
        return False


if __name__ == "__main__":
    # test 
    s = Solution()
    import math
    def truth(num):
        if num > 0 and math.sqrt(num) == int(math.sqrt(num)):
            return True
        else:
            return False
    for num in xrange(-10, 10):
        if truth(num) != s.isPerfectSquare(num):
            print "test failed when num is %d" % num
            break
    print "all test passed!"

