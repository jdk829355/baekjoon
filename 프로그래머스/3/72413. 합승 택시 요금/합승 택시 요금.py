def solution(n, s, a, b, fares):
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i, j, f in fares:
        graph[i][j] = f
        graph[j][i] = f
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    min_fare = graph[s][a] + graph[s][b]
    
    for i in range(1, n+1):
        min_fare = min(min_fare, graph[i][a] + graph[i][b] + graph[s][i])
    
    return min_fare