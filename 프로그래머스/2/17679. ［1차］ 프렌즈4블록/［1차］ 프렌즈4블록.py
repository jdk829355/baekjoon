def solution(m, n, board):
    board = [
        [c for c in row] for row in board
    ]
    
    result = 0
    
    def clear_board():
        nonlocal result
        
        d = (
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 1)
        )
        
        visited = [[0] * n for _ in range(m)]
        
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] == "":
                    continue
                
                values = (
                    board[r+dr][c+dc] for dr, dc in d
                )
                
                
                values = list(set(values))
                
                if len(values) == 1:
                    for dr, dc in d:
                        visited[r+dr][c+dc] = 1
        
        for r in range(m):
            for c in range(n):
                if visited[r][c]:
                    result += 1
                    board[r][c] = ""
        
    
    def drop():
        # 각 컬럼에 대해서 맨 아래부터 시작해서 공백인 경우 그 위에 있는 가장 가까운 값과 교환
        for c in range(n):
            for r in range(m-1, 0, -1):
                if board[r][c] != "":
                    continue
                
                for r2 in range(r-1, -1, -1):
                    if board[r2][c] != "":
                        board[r][c], board[r2][c] = board[r2][c], board[r][c]
                        break
    
    while True:
        tmp = result
        clear_board()
        if result == tmp:
            return result
        drop()
    
        
                    
                        
                