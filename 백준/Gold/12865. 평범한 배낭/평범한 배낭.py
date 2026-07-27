import sys

N, K = map(int, sys.stdin.readline().split())
items = []

for _ in range(N):
    item = list(map(int, sys.stdin.readline().split()))
    items.append({'w': item[0], 'v': item[1]})

# 1차원 배열로 변경
dp = [0 for _ in range(K+1)]
if items[0]['w'] <= K:
    dp = [items[0]['v'] if i >= items[0]['w'] else 0 for i in range(K+1)]
for i in range(1, N):
    w = items[i]['w']
    v = items[i]['v']
    # 역순으로 참조 (가용 용량이 큰 경우를 고려할 때 작은 경우의 값을 쓰므로)
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], v + dp[j-w])

print(dp[-1])
