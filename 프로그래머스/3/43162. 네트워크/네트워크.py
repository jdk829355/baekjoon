def solution(n, computers):
    from collections import deque
    def dfs(st: int):
        q = deque()
        q.append(st)
        
        while len(q):
            p = q.pop()
            for i in range(n):
                if computers[p][i]:
                    computers[p][i] = 0
                    computers[i][p] = 0
                    q.append(i)
    cnt = 0
    for i in range(n):
        if any(computers[i]):
            cnt += 1
            dfs(i)
    return cnt
        
                
