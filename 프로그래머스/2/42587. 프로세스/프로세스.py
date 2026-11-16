def solution(priorities, location):
    processes = [(priorities[i], i) for i in range(len(priorities))]
    
    run_cnt = 0
    
    while processes:
        p, idx = processes.pop(0)
        if all(op <= p for op, _ in processes):
            run_cnt += 1
            if idx == location:
                return run_cnt
        else:
            processes.append((p, idx))