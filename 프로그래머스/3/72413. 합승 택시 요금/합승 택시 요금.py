def solution(n, s, a, b, fares):
    """
    플로이드 와셜로 풀긴 했는데 전체를 시작점으로 고려하는 게 아니라 들러야하는 정점이 정해져 있음 (a, b, s)
    그래서 굳이...?? 그냥 다익스트라를 a, b, s에 대해 쓰고 메모리를 좀 더 쓰면 시간 복잡도는 줄일 수 있지 않을까
    """
    import heapq as hq
    
    adj = [[] for _ in range(n+1)]
    
    for i, j, f in fares:
        adj[i].append((j, f))
        adj[j].append((i, f))
    
    dist_from = {
        s: [float('inf')] * (n+1) for s in ('s', 'a', 'b')
    }
    
    dist_from['s'][s] = 0
    dist_from['a'][a] = 0
    dist_from['b'][b] = 0
    
    
    pq = []
    
    hq.heappush(pq, (0, s, 's'))
    hq.heappush(pq, (0, a, 'a'))
    hq.heappush(pq, (0, b, 'b'))
    
    while pq:
        dist, p, sym = hq.heappop(pq)
        
        if dist > dist_from[sym][p]:
            continue
        
        for v, w in adj[p]:
            if dist_from[sym][v] > dist_from[sym][p] + w:
                dist_from[sym][v] = dist_from[sym][p] + w
                hq.heappush(pq, (dist_from[sym][v], v, sym))
    
    
    min_fare = float('inf')
    for i in range(1, n+1):
        min_fare = min(min_fare, dist_from['s'][i] + dist_from['a'][i] + dist_from['b'][i])
    
    return min_fare