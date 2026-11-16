def solution(land):
    N = len(land)
    dp = [[-1] * 4 for _ in range(N)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = max((land[i][j] + dp[i-1][idx]) for idx in range(4) if idx != j)
    
    return max(dp[-1])