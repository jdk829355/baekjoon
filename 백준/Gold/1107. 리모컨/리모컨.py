import sys

target_ch = int(sys.stdin.readline().strip())

num_broken = int(sys.stdin.readline().strip())
broken = list(sys.stdin.readline().strip().split())

cur_ch = 100

def check_only_plus_minus(target_ch: int, cur_ch: int):
    return abs(target_ch-cur_ch)

def check(target_ch: int, broken: list[str]):
    if sum(map(int, broken)) == 45:
        # 0밖에 안 남은 경우
        return abs(target_ch)+1

    ch_upper = target_ch
    # check upper
    while True:
        if all(c not in broken for c in str(ch_upper)):
            break
        else:
            ch_upper += 1

    # check lower
    ch_lower = target_ch
    while ch_lower >= 0:
        if all(c not in broken for c in str(ch_lower)):
            break
        else:
            ch_lower -= 1
    if ch_lower == -1:
        return abs(target_ch-ch_upper)+len(str(ch_upper))

    return min(map(lambda x: abs(target_ch-x) + len(str(x)), (ch_lower, ch_upper)))



if num_broken == 10:
    print(check_only_plus_minus(target_ch, cur_ch))
elif num_broken == 0:
    print(min(len(str(target_ch)),
              abs(target_ch-cur_ch)
              ))
else:
    print(
        min(
            check_only_plus_minus(target_ch, cur_ch),
            check(target_ch, broken),
        )
    )
