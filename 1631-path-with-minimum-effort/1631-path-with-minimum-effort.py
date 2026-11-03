class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        import heapq as hq
        nrow = len(heights)
        ncol = len(heights[0])
        
        d = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]


        get_adj = lambda r, c : [(r+dr, c+dc, abs(heights[r+dr][c+dc] - heights[r][c])) for dr, dc in d if 0<=r+dr<nrow and 0<=c+dc<ncol]

        effort = [[float('inf')]*ncol for _ in range(nrow)]
        effort[0][0] = 0

        pq = [(0, 0, 0)] # effort, row, col

        while pq:
            e, r, c = hq.heappop(pq)

            if e > effort[r][c]:
                continue
            
            for new_r, new_c, w in get_adj(r,c):
                new_effort = max(w, effort[r][c])
                if effort[new_r][new_c] > new_effort:
                    effort[new_r][new_c] = new_effort
                    hq.heappush(pq, (effort[new_r][new_c], new_r, new_c))
        
        return effort[nrow-1][ncol-1]