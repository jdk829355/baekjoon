def solution(begin, target, words):
    if target not in words:
        return 0
    
    def is_adj(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]: cnt += 1
            if cnt > 1: return False
        return cnt
    
    from collections import deque, defaultdict
    q = []
    visited = set()
    visited.add(begin)
    q.append(begin)
    
    path = defaultdict(int)
    
    while len(q):
        p = q.pop(0)
        
                
        for x in words:
            if is_adj(p, x) and x not in visited:
                visited.add(x)
                q.append(x)
                path[x] = path[p] + 1
                if x == target:
                    break
                
    
    return path[target]
