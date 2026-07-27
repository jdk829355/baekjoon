import sys
from collections import deque, defaultdict

N, M, V = map(int, sys.stdin.readline().strip().split())

vertices = defaultdict(list)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    if y not in vertices[x]:
        vertices[x].append(y)
    if x not in vertices[y]:
        vertices[y].append(x)   

for i in range(1,N+1):
    vertices[i].sort()

q = deque()
s = deque()
q.append(V)
s.append(V)

dfs_visited = []
bfs_visited = []

# dfs
while len(s):
    node = s.pop()
    if node in dfs_visited:
        continue

    dfs_visited.append(node)
    adj_node = vertices[node]

    for i in adj_node[::-1]:
        s.append(i)

# bfs
while len(q):
    node = q.popleft()
    if node in bfs_visited:
        continue

    bfs_visited.append(node)
    adj_node = vertices[node]

    for i in adj_node:
        q.append(i)

print(" ".join(map(str, dfs_visited)))
print(" ".join(map(str, bfs_visited)))
