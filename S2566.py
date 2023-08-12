numbers = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_x, max_y = 0, 0

for y in range(9):
    for x in range(9):
        if max_value < numbers[y][x]:
            max_value = numbers[y][x]
            max_x = x
            max_y = y

print(max_value)
print(max_y + 1, max_x + 1)
