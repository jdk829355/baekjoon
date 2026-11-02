class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        prob = [0] * n

        for idx in range(len(edges)):
            i, j = edges[idx]
            p = succProb[idx]

            adj[i].append((j, p))
            adj[j].append((i, p))

        
        import heapq as hq

        prob[start_node] = 1
        pq = [(-1, start_node)]

        while pq:
            p, u = hq.heappop(pq)
            p *= -1

            if p < prob[u]:
                continue
            
            for v, w in adj[u]:
                if prob[v] < prob[u] * w:
                    prob[v] = prob[u]*w
                    hq.heappush(pq, (-prob[v], v))
        
        return prob[end_node] 