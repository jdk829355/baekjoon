import sys

n = int(sys.stdin.readline().strip())
nums= list(map(int, sys.stdin.readline().strip().split()))
nums.sort()

left = 0
right = n-1
cur = 2000000000
l, r = -1, -1

while left < right:
    s = nums[left] + nums[right]
    if abs(s) < cur:
        cur, l, r = abs(s), nums[left], nums[right]

    if s > 0:
        right -= 1
    elif s < 0:
        left += 1
    else:
        break

print(l, r)
