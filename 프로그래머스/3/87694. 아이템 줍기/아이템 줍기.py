def solution(rectangle, characterX, characterY, itemX, itemY):
    map =[[0] * 200 for _ in range(200)]
    
    rectangle = [ [x*2 for x in r] for r in rectangle]
    
    for r in rectangle:
        for y in range(r[1], r[3]+1):
            for x in range(r[0], r[2] + 1):
                map[y][x] = 1

    for r in rectangle:
        for y in range(r[1]+1, r[3]):
            for x in range(r[0]+1, r[2]):
                map[y][x] = 0
                
    
    from collections import deque, defaultdict
    
    q = deque()
    visited = set()
    st, en = (characterY*2, characterX*2), (itemY*2, itemX*2)
    path = defaultdict(int)
    
    q.append(st)
    visited.add(st)
    
    ds = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )
    
    while len(q):
        p = q.popleft()
        
        if p == en:
            break
            
        for d in ds:
            new = (p[0] + d[0], p[1] + d[1])
            new_v = map[new[0]][new[1]]
            
            if 0 < new[0] < 101 and 0 < new[1] < 101 and new_v == 1 and new not in visited:
                q.append(new)
                visited.add(new)
                path[new] = path[p] + 1
                
    return (path[en])//2