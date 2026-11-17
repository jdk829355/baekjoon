def solution(maps):
    # 가중치 없는 그래프 + 최단거리다? -> BFS
    # 다만, 레버를 거쳐야 함.
    # 근데 s -> l, e가 가능하다 해서 s -> l -> e가 가능한가?
    # 그러면 bfs를 s에서 시작으로 한 번 하고 l에서 시작으로 한 번 해서 각 경로를 이여야겠네
    
    nr = len(maps)
    nc = len(maps[0])
    
    from collections import deque
    d = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )
    
    L = (-1, -1)
    S = (-1, -1)
    E = (-1, -1)
    
    for r in range(nr):
        for c in range(nc):
            if maps[r][c] == 'L':
                L = (r, c)
            elif maps[r][c] == 'E':
                E = (r, c)
            elif maps[r][c] == 'S':
                S = (r, c)
    
    def bfs(r, c, target):
        visited = [[0]* nc for _ in range(nr)]
        dist = [[float("inf")] * nc for _ in range(nr)]
        dist[r][c] = 0
        q = deque()
        q.append((r,c))
        visited[r][c] = 1
        
        while q:
            rr, cc = q.popleft()
            
            for dr, dc in d:
                newr, newc = rr + dr, cc + dc
                if 0<=newr<nr and\
                0<=newc<nc and\
                maps[newr][newc] != 'X' and\
                not visited[newr][newc]:
                    q.append((newr, newc))
                    visited[newr][newc] = 1
                    dist[newr][newc] = dist[rr][cc] + 1
                    if maps[newr][newc] == target:
                        return dist[newr][newc]
        return -1
    
    d1 = bfs(S[0], S[1], 'L')
    if d1 == -1:
        return -1
    
    d2 = bfs(L[0], L[1], 'E')
    if d2 == -1:
        return -1
    
    return d1+d2
                    