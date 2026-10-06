def solution(operations):
    import heapq as hq
    from collections import defaultdict
    
    operations = [(x[0], int(x[2:]))  for x in operations]
    
    max_h, min_h = [], []
    
    deleted = set() # id
    
    id = 0
    for op, arg in operations:
        
        while max_h and max_h[0][1] in deleted:
                        hq.heappop(max_h)
                
        while min_h and min_h[0][1] in deleted:
                        hq.heappop(min_h)
                
        match (op, arg):
            case ('I', arg):
                hq.heappush(max_h, (-arg, id))
                hq.heappush(min_h, (arg, id))
                id += 1
            case ('D', arg) if arg > 0:
                if max_h:
                    item = hq.heappop(max_h)
                    deleted.add(item[1])
            case ('D', arg) if arg < 0:
                if min_h:
                    item = hq.heappop(min_h)
                    deleted.add(item[1])
            case _:
                pass
    
    while max_h and max_h[0][1] in deleted:
        hq.heappop(max_h)
                
    while min_h and min_h[0][1] in deleted:
        hq.heappop(min_h)
    
    res = [0, 0]
    
    if min_h:
        res[1] = hq.heappop(min_h)[0]
    
    if max_h:
        res[0] = -hq.heappop(max_h)[0]
    
    return res