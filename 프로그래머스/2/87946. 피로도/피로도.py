def solution(k, dungeons):
    # k: 현재 피로도
    # dungeons: [[최소 필요, 소모]]
    
    result = 0
    
    def solve(k, left_dungeons):
        nonlocal result
        result = max(result, len(dungeons) - len(left_dungeons))
        n = len(left_dungeons)
        
        for _ in range(n):
            d = left_dungeons.pop(0)
            required, cost = dungeons[d]
            if k >= required:
                k -= cost
                solve(k, left_dungeons)
                k += cost
            left_dungeons.append(d)
                
    solve(k, [i for i in range(len(dungeons))])
    return result
            
                        