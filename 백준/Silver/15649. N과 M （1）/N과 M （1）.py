import sys

N, M = (i for i in sys.stdin.readline().split())
res = []
check = [False]*(int(N)+1)

def solve(st: str):
    if len(st) == int(M):
        res.append(st)
        return 
    
    for x in range(1, int(N)+1):
        if not check[x]:
            check[x] = True
            solve(st+str(x))
            check[x] = False

solve("")
res.sort()
for r in res:
    sys.stdout.write(" ".join(r) + "\n")
