from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

arr = list(int(input()) for _ in range(N))

arr.sort()

def binary_search(S, E):
    global M

    mid = (S + E) // 2

    cnt = 0

    if mid == S or mid == E:
        for i in arr:
            cnt += i // E

        if cnt >= M:
            print(E)
            quit()
        else:
            print(mid)
            quit()


    for i in arr:
        cnt += i // mid
        if cnt >= M:
            break

    if cnt < M:
        binary_search(S, mid)
    elif cnt > M:
        binary_search(mid, E)
    else:
        binary_search(mid, E)

if N != 1:
    binary_search(1, arr[-1])
else:
    for i in range(arr[0], 0, -1):
        if arr[0] // i >= M:
            print(i)
            quit()