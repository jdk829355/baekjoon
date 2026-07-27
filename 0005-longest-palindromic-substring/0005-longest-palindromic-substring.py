class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        def expand(a, b):
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1

            return (a+1, b-1)
        
        res = s[0]
        for i in range(n-1):
            e = expand(i, i+1)
            o = expand(i, i+2)
            res = max(res, s[e[0]:e[1]+1], s[o[0]:o[1]+1], key = len)

        return res