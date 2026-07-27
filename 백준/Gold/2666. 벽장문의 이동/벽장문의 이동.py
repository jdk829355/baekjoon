import sys

N = int(sys.stdin.readline())
left, right = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline())

to_visit = [int(sys.stdin.readline()) for _ in range(M)]

def _count_movement(left: int, right: int, target: int) -> list[tuple[int, int, int]]:
    # 타겟이 열린 두 벽장 사이에 있는 경우
    if left < target < right:
        return [(left, target, right-target), (target, right, target - left)]
    
    # 타겟이 열린 두 벽장의 오른/왼쪽에 있는 경우
    if target > right:
        return [(left, target, target-right), (right, target, target-left)]
    if target < left:
        return [(target, right, left-target), (target, left, right-target)]
    # 타겟이 이미 열려있는 경우
    return [(left, right, 0)]

def solve():
    dp = {
    (left, right): 0
    }

    for target in to_visit:
        new_dp = {}
        for item in dp.items():
            res = _count_movement(item[0][0], item[0][1], target)
            for r in res:
                new_dp[(r[0], r[1])] = min(new_dp.get((r[0], r[1]), float('inf')), r[2]+item[1])
        dp = new_dp
    return min(dp.values())

print(solve())
