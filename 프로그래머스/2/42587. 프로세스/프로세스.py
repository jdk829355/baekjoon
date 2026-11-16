def solution(priorities, location):
    from collections import deque
    processes = deque([(priorities[i], i) for i in range(len(priorities))])
    cnt = [0] * 11
    
    for p in priorities:
        cnt[p] += 1
        
    run_cnt = 0
    
    while processes:
        p, idx = processes.popleft()
        if any(c for c in cnt[p+1:]):
            processes.append((p, idx))
        else:
            run_cnt += 1
            cnt[p] -= 1
            if idx == location:
                return run_cnt