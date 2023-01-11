class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        tmp = int((len(s) - len(s)%2)/2)
        index = 0
        for j in range(tmp):
            if s[j] != s[len(s) - j - 1]: index = 1
        if index == 0: return True
        if index == 1: return False
