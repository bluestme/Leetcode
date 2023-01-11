class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        index = 0
        r = list()
        if s[0] == "-": 
            r.append("-")
            s = s[1:]
        slen = len(s)
        for i in range(slen):
            if s[slen - i - 1] != '0': index = 1
            if index == 1: r.append(s[slen - i - 1])
        out = 0
        if r!= []: out = int("".join(r))
        if out > (2**31 - 1) or out < (-2**31): out = 0
        return out
