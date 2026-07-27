import sys

n:int = int(sys.stdin.readline().strip())
arr: list[int] = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

memo = [(0, 0) for _ in range(n+1)]

if n==1:
    print(arr[0])
elif n==2:
    print(arr[0]+arr[1])
elif n==3:
    print(arr[2]+max(arr[0], arr[1]))
else:
    memo[1], memo[2], memo[3] = (arr[0], arr[0]), (arr[1]+ arr[0], arr[1]), (arr[1]+arr[2], arr[0]+arr[2])

    for i in range(4, n+1):
        memo[i] = (memo[i-1][1]+arr[i-1], max(memo[i-2])+arr[i-1])

    print(max(memo[n]))
