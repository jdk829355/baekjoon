class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for x in range(1, n):
            i, j = 0, x
            while j < n:
                if j-i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                i, j = i+1, j+1
        return max((s[i:j+1] for i in range(n) for j in range(i, n) if dp[i][j]), key=len)