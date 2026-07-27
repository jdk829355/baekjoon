def solution(diffs, times, limit):
    def level_to_time(level):
        n = len(diffs)
        _time = 0
        for i in range(n):
            if(diffs[i] <= level):
                _time += times[i]
            else:
                _time += (diffs[i] - level)*(times[i] + times[i-1]) + times[i]
        return _time
    
    st, en = 1, max(diffs)

    
    while (st < en):
        mid = (st + en)//2
        time = level_to_time(mid)
        
        if(time <= limit):
            en = mid
        else:
            st = mid + 1
           
    return st
