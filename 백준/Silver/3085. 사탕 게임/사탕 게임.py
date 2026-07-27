import sys

N = int(sys.stdin.readline().strip())

candy_map = []
for i in range(N):
    row = sys.stdin.readline().strip()
    row_list = []
    for j in range(N):
        row_list.append(row[j])
    candy_map.append(row_list)

def check_row(row: int) -> int:
    max_candies = 1 

    # check row
    col = 0
    candies = 0
    c = candy_map[row][col]
    while col < N:
        if c == candy_map[row][col]:
            candies += 1
        else:
            max_candies = max(max_candies, candies)
            c = candy_map[row][col]
            candies = 1
        col += 1
    max_candies = max(max_candies, candies)

    return max_candies

def check_col(col:int) -> int:
    max_candies = 1 

    # check col
    row = 0
    candies = 0
    c = candy_map[row][col]
    while row < N:
        if c == candy_map[row][col]:
            candies += 1
        else:
            max_candies = max(max_candies, candies)
            c = candy_map[row][col]
            candies = 1
        row += 1
    max_candies = max(max_candies, candies)
    return max_candies


def solve():
    done = {
        "row": [],
        "col": []
    }
    max_candies = 1
    for row in range(N):
        for col in range(N-1):
            if max_candies == N: return N

            if candy_map[row][col] != candy_map[row][col+1]:
                candy_map[row][col], candy_map[row][col+1] = candy_map[row][col+1], candy_map[row][col]
                max_candies = max(max_candies, check_col(col), check_col(col+1), check_row(row))
                candy_map[row][col], candy_map[row][col+1] = candy_map[row][col+1], candy_map[row][col]
            else:
                target = [max_candies]
                if col not in done["col"]:
                    done["col"].append(col)
                    target.append(check_col(col))

                if row not in done["row"]:
                    done["row"].append(row)
                    target.append(check_row(row))

                max_candies = max(target)

    for col in range(N):
        for row in range(N-1):
            if max_candies == N: return N

            if candy_map[row+1][col] != candy_map[row][col]:
                candy_map[row+1][col], candy_map[row][col] = candy_map[row][col], candy_map[row+1][col]
                max_candies = max(max_candies, check_row(row), check_row(row+1), check_col(col))
                candy_map[row+1][col], candy_map[row][col] = candy_map[row][col], candy_map[row+1][col]
            else:
                target = [max_candies]
                if col not in done["col"]:
                    done["col"].append(col)
                    target.append(check_col(col))

                if row not in done["row"]:
                    done["row"].append(row)
                    target.append(check_row(row))

                max_candies = max(target)


    return max_candies

print(solve())
