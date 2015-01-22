class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_table = {}
        for index1, el in enumerate(num, start = 1):
            if target - el in hash_table:
                index2 = hash_table[target - el]
                if index1 < index2:
                    return (index1, index2)
                else:
                    return (index2, index1)
            else:
                hash_table[el] = index1
