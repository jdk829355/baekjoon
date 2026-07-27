from sys import stdin

N = int(stdin.readline())
cols = [False]*N
sub = [False]*(N*2+1)
add = [False]*(2*N-1)
count = 0


def recur(row: int):
    if row == N:
        global count
        count += 1
        return 
    
    for col in range(N):
        if not cols[col] and not sub[(row-col)+N-1] and not add[row+col]:
            cols[col] = True
            sub[(row-col)+N-1] = True
            add[row+col] = True
            recur(row+1)
            cols[col] = False
            sub[(row-col)+N-1] = False
            add[row+col] = False
recur(0)
print(count)
