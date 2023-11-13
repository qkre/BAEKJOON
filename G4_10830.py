import copy

N, B = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))

now = copy.deepcopy(arr)

for _ in range(B):
    temp = list([1] * N for _ in range(N))
    for i in range(N):
        for j in range(N):
            c = 0
            for k in range(N):
                c += now[i][k]*arr[k][j] % 1000
            temp[i][j] = c
    now = temp

print(now)
