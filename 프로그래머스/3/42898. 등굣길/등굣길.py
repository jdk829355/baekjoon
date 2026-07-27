def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
        
    def get_count(y, x):
        if y >= 0 and x >= 0 and dp[y][x] != -1:
            return dp[y][x]
        else:
            return 0
    
    for x in range(m):
        for y in range(n):
            if dp[y][x] == -1 or (not y and not x):
                continue
            dp[y][x] = get_count(y-1, x) + get_count(y, x-1)
            
    return dp[n-1][m-1]%1000000007
