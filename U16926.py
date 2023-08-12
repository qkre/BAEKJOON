import sys
import copy

input = sys.stdin.readline

N, M, R = map(int, input().split())

cube = [list(map(int, input().split())) for _ in range(N)]


def testPrint(cube):
    for i in cube:
        for j in i:
            print(j, end="\t")
        print()


def printCube(cube):
    for i in cube:
        print(*i)


def push_left(X, Y, current_cube, new_cube, count):
    for i in range(count - 1):
        new_cube[Y][X - i - 1] = current_cube[Y][X - i]


def push_down(X, Y, current_cube, new_cube, count):
    for i in range(count - 1):
        new_cube[Y + i + 1][X] = current_cube[Y + i][X]


def push_right(X, Y, current_cube, new_cube, count):
    for i in range(count - 1):
        new_cube[Y][X + i + 1] = current_cube[Y][X + i]


def push_up(X, Y, current_cube, new_cube, count):
    for i in range(count - 1):
        new_cube[Y - i - 1][X] = current_cube[Y - i][X]


ans_cube = copy.deepcopy(cube)

# R = R % ((N + M - 2) * 2)

for _ in range(R):
    ans_cube = copy.deepcopy(cube)
    for i in range(N):
        startX, endX = i, M - i - 1
        startY, endY = i, N - i - 1
        new_cube = copy.deepcopy(ans_cube)
        if startX >= endX or startY >= endY:
            break
        push_left(endX, startY, ans_cube, new_cube, M - i * 2)
        push_down(startX, startY, ans_cube, new_cube, N - i * 2)
        push_right(startX, endY, ans_cube, new_cube, M - i * 2)
        push_up(endX, endY, ans_cube, new_cube, N - i * 2)
        ans_cube = copy.deepcopy(new_cube)

    cube = copy.deepcopy(ans_cube)

printCube(cube)
