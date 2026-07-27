import sys
from collections import Counter

M, N = map(int, sys.stdin.readline().strip().split())

universe: list[tuple] = []

def normalize(arr) -> tuple:
    nums_ordered = sorted(list(set(arr)))
    map_lt_num = {num:cnt for cnt, num in enumerate(nums_ordered)}

    arr = list(map(lambda x: map_lt_num[x], arr))
    return tuple(arr)

for _ in range(M):
    universe.append(normalize(list(map(int, sys.stdin.readline().strip().split()))))

cnt = Counter(universe)
res = 0
for value in cnt.values():
    if value >1:
        res += value*(value-1)//2
print(res)
