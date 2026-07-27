import sys

memo = {}

def solve(day, numOne, numHalf) -> int:
    if day == 0:
        return 1
    
    if (day, numOne, numHalf) in memo:
        return memo[(day, numOne, numHalf)]
    
    res = 0
    if numHalf > 0:
        res += solve(day-1, numOne, numHalf-1)
    if numOne > 0:
        res += solve(day-1, numOne-1, numHalf+1)
    memo[(day, numOne, numHalf)] = res
    return res

result = []
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    result.append(str(solve(2*N, N, 0)))
print("\n".join(result))
