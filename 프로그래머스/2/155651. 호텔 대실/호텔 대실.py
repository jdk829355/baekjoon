def solution(book_time):
    '''
    최소한의 객실. 한 번 사용한 객실은 퇴실 기준 10분 청소 (청소도 방을 쓰는 거랑 똑같은 거 아닌가 그러면)
    입실 시각 기준으로 정렬했을 때, 0 ~ i까지가 최적이면, i+1은 입실 시각에서 필요한 방의 개수가 i+1에서 필요한 방의 개수의 최소임. 
    왜냐? 그 이후로 넘어가면 차지된 방의 개수가 유지 혹은 줄어듦. 결국 필요한 방의 개수는 입실 시각에 결정 남. 
    '''
    
    n = len(book_time)
    
    # 분단위 정수 표현으로 변경
    for i in range(n):
        book_time[i] = [60*int(x[:2]) + int(x[3:5]) for x in book_time[i]]
        book_time[i][1] += 10
    
    # 시작 시점 기준으로 정렬
    book_time.sort()
    res = 0
    
    for i in range(n):
        acc = 0
        for j in range(i+1):
            if book_time[i][0] < book_time[j][1]:
                acc += 1
        res = max(res, acc)
    return res