import itertools
import copy

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
perms = [i for i in range(K)]
permutaitons = list(itertools.permutations(perms, K))
rotations = [list(map(int, input().split())) for _ in range(K)]

ans = 100000000000000


def push_right(original, arr, x, y, c):
    for i in range(1, c):
        before = original[y][x + i - 1]
        arr[y][x + i] = before


def push_down(original, arr, x, y, c):
    for i in range(1, c):
        before = original[y + i - 1][x]
        arr[y + i][x] = before


def push_left(original, arr, x, y, c):
    for i in range(1, c):
        before = original[y][x - i + 1]
        arr[y][x - i] = before


def push_up(original, arr, x, y, c):
    for i in range(1, c):
        before = original[y - i + 1][x]
        arr[y - i][x] = before


for perm in permutaitons:
    new_arr = copy.deepcopy(arr)
    for i in perm:
        result = copy.deepcopy(new_arr)
        r, c, s = rotations[i]
        for i in range(1, s + 1):
            push_right(result, new_arr, c - i - 1, r - i - 1, i * 2 + 1)
            push_down(result, new_arr, c + i - 1, r - i - 1, i * 2 + 1)
            push_left(result, new_arr, c + i - 1, r + i - 1, i * 2 + 1)
            push_up(result, new_arr, c - i - 1, r + i - 1, i * 2 + 1)

    for col in new_arr:
        ans = min(ans, sum(col))

print(ans)
