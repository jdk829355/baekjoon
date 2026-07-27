import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(board, x, y, numr, numc):
    d = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    Q = deque()
    Q.append((x, y))
    board[x][y] = 0

    while len(Q):
        curx, cury = Q.popleft()

        for dx, dy in d:
            if 0 <= (newx := dx+curx) < numr and 0 <= (newy := dy+cury) < numc and board[newx][newy] == 1:
                Q.append((newx, newy))
                board[newx][newy] = 0
    

def solve_case():
    c, r, n = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(c)] for _ in range(r)]
    for _ in range(n):
        col, row = map(int, sys.stdin.readline().split())
        board[row][col] = 1
    cnt = 0
    for row in range(r):
        for col in range(c):
            if board[row][col] == 1:
                bfs(board, row, col, r, c)   
                cnt += 1
    return cnt

res = []
for _ in range(T):
    res.append(str(solve_case()))
print("\n".join(res))
