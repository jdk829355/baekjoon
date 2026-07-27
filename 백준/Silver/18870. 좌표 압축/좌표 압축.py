import sys

N = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().strip().split()))
nums = sorted(list(set(target)))

def bin_search(x: int) -> int:
    s, e = 0, len(nums)-1
    while s <= e:
        mid = (s+e)//2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            e = mid - 1
        else:
            s = mid + 1 
    return -1

print(" ".join(str(bin_search(i)) for i in target))
