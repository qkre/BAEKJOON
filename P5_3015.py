from sys import stdin

input = stdin.readline

N = int(input())

arr = list(int(input()) for _ in range(N))
cnt = 0

for i in range(N):
    A = arr[i]
    stack = [0]

    for j in range(i + 1, N):
        if stack[-1] > arr[j]:
            break
        stack.append(arr[j])
        cnt += 1

print(cnt)
