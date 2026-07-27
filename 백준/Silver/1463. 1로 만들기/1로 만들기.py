import sys

n:int = int(sys.stdin.readline().strip())

length = max(n+1, 4)
arr: list[int] = [-1]*length
arr[1] = 0
arr[2] = 1
arr[3] = 1

if n < 4:
    print(arr[n])
else:
    for i in range(4, n+1):
        arr[i] = min(
            arr[i-1]+1,
            arr[i//2]+1 if i%2==0 else length,
            arr[i//3]+1 if i%3==0 else length
        )
    print(arr[n])
