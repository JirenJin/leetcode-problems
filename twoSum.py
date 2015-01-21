class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # hash table O(1) to find the (target - key)
        hash_table = {}
        for i in range(len(num)):
            # use num[i] as key of hash_table
            # have to solve multi values of same key's problem
            # This is the one of the methods
            try:
                hash_table[num[i]].append(i + 1)
            except KeyError:
                hash_table[num[i]] = [i + 1]

        for key1, value1 in hash_table.items():
            key2 = target - key1
            if key2 in hash_table:
                # maybe 2 numbers we want are equal
                if key2 != key1:
                    value2 = hash_table[key2]
                    if value1[0] < value2[0]:
                        return (value1[0], value2[0])
                    else:
                        return (value2[0], value1[0])
                else:
                    if len(value1) >= 2:
                        return (value1[0], value1[1])
        else:
            return None

if __name__ == '__main__':
    import random
    numbers = [None] * 100
    for i in range(100):
        numbers[i] = random.randint(0, 100)

a = Solution()

answer = a.twoSum(numbers, 54)
print answer
print numbers[answer[0] - 1], numbers[answer[1] - 1]
