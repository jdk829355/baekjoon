def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    for i, j in edge:
        adj[i].append(j)
        adj[j].append(i)
    
    
    from collections import deque, defaultdict
    
    dists = [0]*(n+1)
    visited = [0] * (n+1)
    
    q = deque()
    q.append(1)
    visited[1] = 1
    max_dist = -1
    
    while q:
        p = q.popleft()
        
        for new in adj[p]:
            if not visited[new]:
                q.append(new)
                visited[new] = 1
                dists[new] = dists[p] + 1
                max_dist = dists[new]

    return len([x for x in dists if x == max_dist])