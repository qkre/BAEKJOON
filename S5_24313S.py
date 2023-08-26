a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


def f(n, a1, a0):
    return a1 * n + a0


for i in range(n0, 101):
    if f(i, a1, a0) > c * i:
        print(0)
        quit()

print(1)
