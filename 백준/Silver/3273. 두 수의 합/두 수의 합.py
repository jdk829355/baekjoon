import sys

n = int(sys.stdin.readline().strip())
nums= list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
x = int(sys.stdin.readline().strip())

count = 0
left = 0
right = n-1

while left < right:
    res = nums[left] + nums[right]
    if res > x:
        right -= 1
    elif res < x:
        left += 1
    else:
        count += 1
        right -= 1
        left += 1
print(count)
