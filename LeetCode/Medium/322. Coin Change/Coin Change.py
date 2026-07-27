class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [float("INF")]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            cands = [dp[i-c] + 1 for c in coins if i-c >= 0]
            dp[i] = min(dp[i], min(
                cands if len(cands) else [float("INF")]
            ))

        return dp[amount] if dp[amount] < float("INF") else -1
