def solution(N, road, K):
    adj = [[] for _ in range(N+1)]
    time = [float('inf')] * (N+1)
    time[1] = 0
    
    for i, j, w in road:
        adj[i].append((j, w))
        adj[j].append((i, w))
    
    import heapq as hq
    
    
    pq = [(0, 1)]
    
    while pq:
        t, u = hq.heappop(pq)
        
        if t > time[u] or time[u] > K:
            continue
        
        for v, dt in adj[u]:
            if time[v] > time[u] + dt:
                time[v] = time[u] + dt
                hq.heappush(pq, (time[v], v))
        
    return len([x for x in time if x <= K])