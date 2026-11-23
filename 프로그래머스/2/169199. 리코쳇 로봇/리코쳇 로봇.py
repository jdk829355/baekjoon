def solution(board):
    # bfs 변형인듯
    # visited 처리가 애매한데...
    
    nrow, ncol = len(board), len(board[0])
    
    def get_target(r, c, d):
        while (0<=r+d[0]<nrow and 0<=c+d[1]<ncol and board[r+d[0]][c+d[1]] in ('.', 'G', 'R')):
            r += d[0]
            c += d[1]
        return (r, c)
    
    from collections import deque
    q = deque()
    visited = [[0] * ncol for _ in range(nrow)]
    path = [[0] * ncol for _ in range(nrow)]
    
    from itertools import product

    for r, c in product(range(nrow), range(ncol)):
        if board[r][c] == 'R':
            q.append((r, c))
            visited[r][c] = 1
            break

    d = (
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    )
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in d:
            newr, newc = get_target(r, c, (dr, dc))
            # 보드 안에 있고, 도달 가능한 거 확실하니까 visite만 점검
            if not visited[newr][newc]:
                visited[newr][newc] = 1
                path[newr][newc] = 1+path[r][c]
                q.append((newr, newc))
                if board[newr][newc] == 'G':
                    return path[newr][newc]
    return -1