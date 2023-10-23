from sys import stdin

input = stdin.readline

N = int(input())

positions = list(list(map(int, input().split())) for _ in range(N))
positions.append(positions[0])
area = 0
for i in range(N):
    area += (
        positions[i][0] * positions[i + 1][1] - positions[i + 1][0] * positions[i][1]
    )

area = abs(area)

print("%.1f" % (area / 2))
