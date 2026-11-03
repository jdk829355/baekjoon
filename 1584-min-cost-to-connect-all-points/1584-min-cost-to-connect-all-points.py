class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        F = []
        W = [[0] * n for _ in range(n)]

        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                W[i][j] = dist
                W[j][i] = dist

        nearest =[-1] * n
        distance =[-1] * n

        for i in range(n):
            nearest[i] = 0
            distance[i] = W[0][i]


        for _ in range(n - 1):
            min = float("inf")
            vnear = -1
            for i in range(1, n):
                if 0 <= distance[i] < min:
                    min = distance[i]
                    vnear = i

            e = (nearest[vnear], vnear, distance[vnear])
            distance[vnear] = -1
            F.append(e)

            for i in range(1, n):
                if distance[i] > W[i][vnear]:
                    distance[i] = W[i][vnear]
                    nearest[i] = vnear
        
        return sum(x[2] for x in F)
