import sys

T = int(sys.stdin.readline())

def solve(n: int) -> int:
    if n <= 2:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[-1]

res = []
for _ in range(T):
    res.append(solve(int(sys.stdin.readline())))

print("\n".join(str(i) for i in res))
