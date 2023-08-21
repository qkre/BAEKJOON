S = list(input())
ZOAC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cursor = 0
time = 0
for alphabet in S:
    if (abs(ZOAC.index(alphabet) + cursor)) < 13:
        time += abs(ZOAC.index(alphabet) - cursor)
        cursor = ZOAC.index(alphabet)
    else:
        time += 26 - (ZOAC.index(alphabet) + cursor)
        cursor = ZOAC.index(alphabet)

print(time)
