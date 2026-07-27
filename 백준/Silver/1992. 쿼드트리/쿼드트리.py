import sys

N = int(sys.stdin.readline())

table = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(N)]


def check(loc: tuple[int, int], n:int) -> int:
    s = 0
    for row in range(loc[0], loc[0]+n):
        for col in range(loc[1], loc[1]+n):
            s+= table[row][col]
    if s == 0:
        return 0
    if s == n*n:
        return 1
    return -1

def recur(loc: tuple[int, int], n:int) -> str:
    if (res:=check(loc, n)) != -1:
        return str(res)
    
    sep = (
        loc,
        (loc[0], loc[1]+n//2),
        (loc[0]+n//2, loc[1]),
        (loc[0]+n//2, loc[1]+n//2)
    )
    res = ""

    for point in sep:
        res += recur(point, n//2)
    return "("+res+")"

print(recur((0, 0), N))
