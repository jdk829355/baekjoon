import sys

n:int = int(sys.stdin.readline().strip())
rgb:list[tuple] = []

for _ in range(n):
    rgb.append(tuple(map(int, sys.stdin.readline().strip().split())))

p = [[0, 0, 0] for _ in range(n)]
p[0] = list(rgb[0])

for i in range(1, n):
    for j in range(3):
        p[i][j] = min(p[i-1][k] for k in range(3) if k!=j) + rgb[i][j]
print(min(p[-1]))
