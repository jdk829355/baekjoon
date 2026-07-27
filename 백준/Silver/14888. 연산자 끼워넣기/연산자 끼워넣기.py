from sys import stdin

N = int(stdin.readline())
nums = [int(i) for i in stdin.readline().split()]
ops = (int.__add__, int.__sub__, int.__mul__, lambda x, y: int(abs(x))//y if x > 0 else -(abs(x)//y))

operations = {
    ops[idx]: int(n) for idx, n in enumerate(stdin.readline().split()) 
}
max_res = -1000000000
min_res = 1000000000

def recur(value: int, idx: int):
    if idx == N:
        global min_res, max_res
        max_res = max(max_res, value)
        min_res = min(min_res, value)
        return
    
    for op, cnt in operations.items():
        if cnt > 0:
            operations[op] -= 1
            recur(op(value, nums[idx]), idx+1)
            operations[op] += 1
recur(nums[0], 1)

print(max_res)
print(min_res)
