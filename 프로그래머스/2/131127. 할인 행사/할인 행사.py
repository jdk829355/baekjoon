def solution(want, number, discount):
    from collections import defaultdict
    left, right = 0, 9
    
    want_map = {}
    is_in_want = defaultdict(int)
    
    for i in range(len(want)):
        want_map[want[i]] = number[i]
        is_in_want[want[i]] = 1
    
    for i in range(10):
        if is_in_want[discount[i]]:
            want_map[discount[i]] -= 1
    
    cnt = 1 if all(x <= 0 for x in want_map.values()) else 0
    
    while right+1 < len(discount):
        if is_in_want[discount[left]]:
            want_map[discount[left]] += 1
        
        if is_in_want[discount[right+1]]:
            want_map[discount[right+1]] -= 1
        
        left, right = left + 1, right + 1
        
        if all(x <= 0 for x in want_map.values()):
            cnt += 1
            
    return cnt