arr = list(list(map(int, input().split())) for _ in range(9))


def check(y, x, target):
    # 좌우
    if arr[y].count(target) != 0:
        return False

    # 상하
    for i in range(9):
        if arr[i][x] == target:
            return False


    # 3*3

    if y < 3:
        y_range = 3
    elif y < 6:
        y_range = 6
    else:
        y_range = 9

    if x < 3:
        x_range = 3
    elif x < 6:
        x_range = 6
    else:
        x_range = 9

    for i in range(y_range - 3, y_range):
        for j in range(x_range - 3, x_range):
            if arr[i][j] == target:
                return False

    return True

def dfs():
    checked = True
    for i in arr:
        if i.count(0) != 0:
            checked = False

    if checked:
        for i in arr:
            print(*i)

        quit()

    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for k in range(1, 10):
                    if check(i, j, k):
                        arr[i][j] = k
                        dfs()
                        arr[i][j] = 0
                return

dfs()