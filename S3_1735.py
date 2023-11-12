arr = list(list(map(int, input().split())) for _ in range(2))

ans = [arr[0][0] * arr[1][1] + arr[0][1] * arr[1][0], arr[0][1] * arr[1][1]]

son = ans[0]
mom = ans[1]

son_divider = []
mom_divider = []
for i in range(1, int(son**0.5)+1):
    if son % i == 0:
        son_divider.append(i)
        son_divider.append(son // i)

for i in range(1, int(mom**0.5)+1):
    if mom % i == 0:
        mom_divider.append(i)
        mom_divider.append(mom // i)

son_divider.sort()
mom_divider.sort()

equal_divider = []

if len(son_divider) < len(mom_divider):
    for i in son_divider:
        if i in mom_divider:
            equal_divider.append(i)
else:
    for i in mom_divider:
        if i in son_divider:
            equal_divider.append(i)


for i in equal_divider:
    if son // i >= 1 and mom // i >= 1:
        son //= i
        mom //= i
    else:
        break


print(son, mom)