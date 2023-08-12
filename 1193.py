X = int(input())

index = 0
count = 1
val = 0

while index < X:
    index += count
    count += 1
    val += 1

result = index - X

if val % 2 == 0:
    m = 1
    s = val
    for i in range(result):
        m += 1
        s -= 1

if val % 2 != 0:
    m = val
    s = 1
    for i in range(result):
        m -= 1
        s += 1

print(f"{s}/{m}")
