import sys

N = int(sys.stdin.readline())

table = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

num_white = 0
num_blue = 0

def check(loc: tuple[int, int], n:int) -> str:
    s = 0
    for row in range(loc[0], loc[0]+n):
        for col in range(loc[1], loc[1]+n):
            s+= table[row][col]
    if s == 0:
        return "w"
    if s == n*n:
        return "b"
    return "n"

def recur(loc: tuple[int, int], n:int):
    if (res:=check(loc, n)) in ("w", "b"):
        global num_blue, num_white
        if res == "w":
            num_white += 1
        elif res == "b":
            num_blue += 1
        return
    
    sep = (
        loc,
        (loc[0]+n//2, loc[1]+n//2),
        (loc[0]+n//2, loc[1]),
        (loc[0], loc[1]+n//2)
    )

    for point in sep:
        recur(point, n//2)

recur((0, 0), N)

print(num_white)
print(num_blue)
