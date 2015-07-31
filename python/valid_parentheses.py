class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        else:
            b_dict = {'(':')', '[':']', '{':'}'}
            stack = []
            for b in s:
                if b in b_dict:
                    stack.append(b)
                else:
                    if not stack or b_dict[stack.pop(-1)] != b:
                        return False
            if not stack:
                return True
            else:
                return False
