def solution(maps):
    from collections import deque, defaultdict
    q = deque()
    q.append((0, 0))
    
    visit = set()
    visit.add((0, 0))
    
    path= defaultdict(int)
    path[(0, 0)] = 1
    
    n, m = len(maps), len(maps[0])
    
    diffs = (
        (-1, 0),
        (0, -1),
        (+1, 0),
        (0, +1)
    )
    
    
    while(len(q)):
        r, c = q.popleft()
        if r == n-1 and c == m-1:
            break
        
        for diff in diffs:
            new_r, new_c = r+diff[0], c+diff[1]
            
            if 0 <= new_r < n and \
               0 <= new_c < m and \
               maps[new_r][new_c] == 1 and \
               (new_r, new_c) not in visit:
            
                path[(new_r, new_c)] = path[(r, c)]+1
                visit.add((new_r, new_c))
                q.append((new_r, new_c))
                
                
    if path[(n-1, m-1)] == 0:
        return -1
    else:
        return path[(n-1, m-1)]
