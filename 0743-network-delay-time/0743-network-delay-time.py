class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        time = [float('inf')]*(n+1)
        time[k] = 0
        time[0] = -1

        for u, v, w in times:
            adj[u].append((v, w))

        import heapq as hq

        pq = [(0, k)]

        while pq:
            w, u = hq.heappop(pq)

            if w > time[u]:
                continue
            
            for v, w2 in adj[u]:
                if time[v] > time[u] + w2:
                    time[v] = time[u] + w2
                    hq.heappush(pq, (time[v], v))

        maxtime = max(time)
        return maxtime if maxtime != float('inf') else -1