from sys import stdin


input = stdin.readline

N = int(input())

arr = list(int(input()) for _ in range(N))

arr.sort()


R = N * 0.15

def round(N):

    decimal = list(str(N).split('.')[1])

    decimal = list(decimal)

    if decimal[0] >= '5':
        return int(N) + 1
    else:
        return int(N)

R = round(R)

arr = arr[R : N - R]

if N - 2 * R != 0:
    ans = sum(arr) / (N - 2 * R)
    ans = round(ans)
    print(ans)
else:
    print(0)