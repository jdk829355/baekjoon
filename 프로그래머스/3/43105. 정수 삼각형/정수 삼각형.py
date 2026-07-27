def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(i+1)] for i in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j < 1:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            
    return max(dp[-1])
