import sys
from collections import deque

me, bro = map(int, sys.stdin.readline().split())

visited = {}
visited[me] = 0

Q = deque()
Q.append(me)
d = [
    lambda x: 2*x,
    lambda x: x-1,
    lambda x: x+1
]

def solve():
    if me == bro:
        return 0
    
    if me > bro:
        return me-bro

    while len(Q):
        loc = Q.popleft()
        steps = visited[loc]

        for d_func in d:
            new_loc = d_func(loc)

            if 0 <= new_loc <= 100000 and new_loc not in visited:
                if new_loc == bro:
                    return steps+1
                Q.append(new_loc)
                visited[new_loc] = steps + 1

print(solve())
