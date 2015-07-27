class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')
        l1 = len(version1)
        l2 = len(version2)
        if l1 > l2:
            version2 += [0] * (l1 - l2)
        else:
            version1 += [0] * (l2 - l1)
        for i, j in zip(version1, version2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1
            else:
                continue
        else:
            return 0
