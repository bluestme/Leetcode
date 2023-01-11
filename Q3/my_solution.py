class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = list()
        substrlen = 0
        index  = 0
        for i in s:
            if i not in substr:
                substr.append(i)
                index = index + 1
                if len(substr) > substrlen:
                    substrlen = len(substr)    
            else:
                if len(substr) > substrlen:
                    substrlen = len(substr)
                index2 = 0
                for j in range(len(substr)):
                    if substr[j] == i:
                        index2 = j + 1
                index = len(substr)
                substr.append(i)
                substr = substr[index2:]
        return substrlen
