class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        map_dict1 = dict()
        map_dict2 = dict()
        for c1, c2 in zip(s, t):
            if c2 not in map_dict1:
                map_dict1[c2] = c1
            else:
                if map_dict1[c2] != c1:
                    return False
            if c1 not in map_dict2:
                map_dict2[c1] = c2
            else:
                if map_dict2[c1] != c2:
                    return False
        else:
            return True
