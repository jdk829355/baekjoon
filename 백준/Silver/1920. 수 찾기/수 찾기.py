import sys

N = int(sys.stdin.readline().strip())
target = sorted(list(map(int, sys.stdin.readline().strip().split())))

M = int(sys.stdin.readline().strip())

def is_in(num: int) -> bool:
    s, e = 0, N-1
    while s <= e:
        mid = (s + e)//2
        if target[mid] == num:
            return True
        elif target[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return False

nums = map(lambda num: '1' if is_in(int(num)) else '0', sys.stdin.readline().strip().split())
print('\n'.join(nums))
