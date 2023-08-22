from sys import stdin

input = stdin.readline

N = int(input())
positions = list(list(map(int, input().split())) for _ in range(N))
on_sight = []

for position in positions:
    x, y = position
    if x != 0 and y != 0:
        m = y / x
    elif x == 0:
        m = "Y"
    elif y == 0:
        m = "X"
    if m not in on_sight:
        on_sight.append(m)

print(len(on_sight))
