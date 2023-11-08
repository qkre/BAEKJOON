import sys

input = sys.stdin.readline

N = int(input())


factorial = [1, 1]

for i in range(2, N):
    if factorial[i - 1] * i > N:
        break
    factorial.append(factorial[i - 1] * i)

if N < 1:
    print("NO")
    quit()


def dfs(depth, now):
    global N

    if now == N:
        print("YES")
        quit()

    elif now > N:
        return

    for i in range(depth, len(factorial)):
        dfs(i + 1, now + factorial[i])


if sum(factorial) < N:
    print("NO")
else:
    for i in range(len(factorial)):
        dfs(i + 1, factorial[i])
    print("NO")
