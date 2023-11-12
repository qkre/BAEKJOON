arr = list(list(map(int, input().split())) for _ in range(2))

ans = [arr[0][0] * arr[1][1] + arr[0][1] * arr[1][0], arr[0][1] * arr[1][1]]

son = ans[0]
mom = ans[1]

d = []

for i in range(1, int(son**0.5)):
    if son % i == 0:
        d.append(i)
        d.append(son // i)

d.sort()


GCF = 1

for i in d:
    if mom % i == 0:
        GCF = i


son //= GCF
mom //= GCF

print(son, mom)
