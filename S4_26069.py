from sys import stdin

input = stdin.readline

N = int(input())

dict = {"ChongChong": True}

cnt = 1
for _ in range(N):
    A, B = input().rstrip().split()

    if A in dict and B not in dict:
        dict[B] = True
        cnt += 1
    elif B in dict and A not in dict:
        dict[A] = True
        cnt += 1

print(cnt)
