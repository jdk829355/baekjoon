import sys

N = int(sys.stdin.readline().strip())
n_list = []
for _ in range(N):
    n_list.append(tuple(map(int, sys.stdin.readline().strip().split())))

n_list.sort(key=lambda x: (x[1], x[0]))

cur = 0
count = 0

for I in n_list:
    if I[0] >= cur:
        count+=1
        cur = I[1]
print(count)
