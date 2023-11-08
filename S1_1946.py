import sys
import copy

input = sys.stdin.readline

T = int(input())

ans = []

for _ in range(T):
    N = int(input())

    arr = list(list(map(int, input().split())) for _ in range(N))

    arr_first = list(sorted(arr, key=lambda x: x[0] + x[1]))

    passed = []

    tmp = []

    first = arr_first[0]

    tmp.append(first)

    for i in range(1, N):
        opponent = arr_first[i]

        if first[0] < opponent[0] and first[1] < opponent[1]:
            continue

        tmp.append(opponent)

    arr_last = list(sorted(tmp, key=lambda x: x[0] + x[1]))

    first = arr_last[0]

    ans = [first]
    for i in range(1, len(arr_last)):
        opponent = arr_last[i]
        if first[0] < opponent[0] and first[1] < opponent[1]:
            continue
        ans.append(opponent)

    print(len(ans))
