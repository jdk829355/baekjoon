def solution(n, times):
    def time_to_n(t, times):
        return sum(t//time for time in times)
    
    st, en = 1, min(times) * n
    
    while(st < en):
        mid = (st+en)//2
    
        if(time_to_n(mid, times) >= n):
            en = mid
        else:
            st = mid+1
    return st
