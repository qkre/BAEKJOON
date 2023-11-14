from sys import stdin
input = stdin.readline

N = int(input())

dict = {}
cnt = 0
for _ in range(N):
    s = input().rstrip()

    if s == 'ENTER':
        dict = {}
    else:
        if s not in dict:
            cnt += 1
            dict[s] = True

print(cnt)