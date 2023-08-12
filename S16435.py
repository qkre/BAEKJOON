import sys

input = sys.stdin.readline

N, L = map(int, input().split())
H = sorted(list(map(int, input().split())))

for height in H:
    if height > L:
        print(L)
        quit()
    L += 1

print(L)
