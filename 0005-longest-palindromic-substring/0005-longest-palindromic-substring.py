class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        res = s[0]

        for x in range(1, n):
            i, j = 0, x
            while j < n:
                if (j-i == 1 and s[i] == s[j]) or (s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    res = max(res, s[i:j+1], key=len)
                i, j = i+1, j+1

        return res