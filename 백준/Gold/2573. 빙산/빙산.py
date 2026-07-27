import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

board = [[int(i) for i in sys.stdin.readline().split()] for _ in range(r)]

d = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def cnt_and_melt():
    """ 녹기 전 빙하 덩어리 개수 출력 + 빙하 녹이기 수행 """
		
    Q = deque()
    visited = set()
    cnt = 0
    melt_map = {}

    for row in range(r):
        for col in range(c):
		        # 빙산 시작점 발견 (방문하지 않았으면서 솟아있는 곳)
            if board[row][col] > 0 and (row, col) not in visited:
		            # 빙산 덩어리 개수 + 1
                cnt += 1
                Q.append((row, col))
                visited.add((row, col))
                
                # bfs 시작
                while len(Q):
                    p = Q.popleft()
                    # 접해있는 바다 수 (점마다 다르므로 여기서 초기화)
                    zero_cnt = 0
                    for dx, dy in d:
                        new_x, new_y = p[0] + dx, p[1] + dy 
                        # 여기는 bfs랑 같음
                        if all((0 <= new_x < r, 
                               0 <= new_y < c,
                               (new_x, new_y) not in visited,
                               board[new_x][new_y] > 0)):

                            Q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                            
                        # 추가된 부분 (접한 바다 수 누적)
                        if all((0 <= new_x < r,
                                0 <= new_y < c,
                                board[new_x][new_y] == 0)):
                        
                                zero_cnt += 1
                    # 한 점에 대한 인접한 점을 모두 봤으면 {점 -> 녹는 높이} 에 저장함
                    melt_map[p] = zero_cnt
    # 빙하 녹이기
    for p, bingha in melt_map.items():
        board[p[0]][p[1]] = max(board[p[0]][p[1]] - bingha, 0)
    # 빙하 덩어리 개수 출력
    return cnt

years= 0
while True:
    cnt = cnt_and_melt()
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(years)
        break
    years += 1
