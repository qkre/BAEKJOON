import sys

input = sys.stdin.readline

N = int(input())

arr = list(list(map(int, input().split())) for _ in range(N))

arr.sort(key=lambda x: (x[1], x[0] + x[1]))
index = 0
cnt = 0
while True:
    cnt += 1
    start = arr[index][0]
    end = arr[index][1]

    valid = False
    for i in range(index + 1, N):
        if arr[i][0] >= end:
            index = i
            valid = True
            break

    if not valid:
        break

print(cnt)
