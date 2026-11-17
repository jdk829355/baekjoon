def solution(sequence, k):
    # 합 = k
    # (길이, 앞 인덱스) 우선순위
    
    N = len(sequence)
    left = right = 0
    s = sequence[0]
    
    if s == k:
        return [0, 0]
    
    import heapq as hq
    # (길이, left, right)
    res = (float("inf"), float("inf"), float("inf")) 
    
    while left <= right and right < N:
        if s == k:
            res = min(res, (right-left, left, right))
            s -= sequence[left]
            if left < right:
                left += 1
            else:
                break
        elif s < k:
            if right < N-1:
                right += 1
            else:
                break
            s += sequence[right]
            
        else:
            s -= sequence[left]
            if left < right:
                left += 1
            else:
                break
    return res[1:]
        