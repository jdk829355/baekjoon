import sys
from collections import deque
from pprint import pprint

r, c = map(int, sys.stdin.readline().split())
board = [[int(i) for i in sys.stdin.readline().split()] for _ in range(r)]
d = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def bfs(start: tuple[int, int]) -> int:
    Q = deque()
    Q.append(start)
    board[start[0]][start[1]] = 0

    size = 0
    while len(Q):
        p = Q.popleft()
        size += 1
        for (dx, dy) in d:
            if 0 <= (new_x := dx + p[0]) < r and 0 <= (new_y := dy + p[1]) < c and board[new_x][new_y]:
                Q.append((new_x, new_y))
                board[new_x][new_y] = 0
    return size

max_size = 0
cnt = 0
for x in range(r):
    for y in range(c):
        if board[x][y]:
            cnt += 1
            max_size = max(bfs((x, y)), max_size)
print(cnt)
print(max_size)
