class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        length = 0
        appeared_list = list()
        for i in range(len(s)):
            if s[i] not in appeared_list:
                appeared_list.append(s[i])
            else:
                if length < len(appeared_list):
                    length = len(appeared_list)
                index = appeared_list.index(s[i])
                appeared_list.append(s[i])
                appeared_list = appeared_list[index + 1:]
            if i == len(s) -1:
                if length < len(appeared_list):
                    length = len(appeared_list)
        return length
