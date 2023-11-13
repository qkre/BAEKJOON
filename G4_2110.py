from sys import stdin

input = stdin.readline

N, C = map(int, input().split())

arr = list(int(input()) for _ in range(N))
wifi = [False] * N
arr.sort()

if C == 2:
    print(arr[-1] - arr[0])
else:
    C -= 2
    wifi[0], wifi[-1] = True, True

    while C > 0:
        C -= 1

        while True:
            mid = (S+E) // 2

            if mid == S or mid == E:
                wifi[mid] = True
                break

            if arr[mid] - arr[S] < arr[E] - arr[mid]:
                S = mid
            else:
                E = mid

    ans = arr[-1]

    S = arr[0]
    for i in range(1, N):
        if wifi[i]:
            ans = min(ans, arr[i] - S)
            S = arr[i]

    print(ans)

