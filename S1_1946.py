import sys
import copy

input = sys.stdin.readline

T = int(input())

ans = []

for _ in range(T):
    N = int(input())

    arr = list(list(map(int, input().split())) for _ in range(N))

    arr_first = list(sorted(arr, key=lambda x: x[0]))
    arr_last = list(sorted(arr, key=lambda x: x[1]))

    not_passed = []

    for i in arr_first:
        for j in range(arr_last.index(i) + 1, N):
            if arr_first.index(i) > arr_first.index(arr_last[j]):
                break
            else:
                if arr_last[j] not in not_passed:
                    not_passed.append(arr_last[j])
    ans.append(N - len(not_passed))
for _ in ans:
    print(_)
