def solution(N, number):
    from collections import defaultdict
    dp = defaultdict(set)
    
    if N == number:
        return 1
    
    dp[1] = set(
        [N]
    )
    dp[2] = set((
        N+N, N-N, N*N, 1, N*11
    ))
    
    n = 2
    while number not in dp[n]:
        n += 1
        if n > 8:
            return -1
        for i in range(1, n):
            for x in dp[i]:
                for y in dp[n-i]:
                    dp[n].add(x+y)
                    dp[n].add(x-y)
                    dp[n].add(x*y)
                    if y != 0:
                        dp[n].add(int(x/y))
        dp[n].add(int(str(N)*n))

    
    return n if n <= 8 else -1
