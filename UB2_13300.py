N, K = map(int, input().split())

room = 0

women = [0] * 6
men = [0] * 6

for _ in range(N):
    sex, grade = map(int, input().split())
    if sex == 0:
        women[grade - 1] += 1

    else:
        men[grade - 1] += 1


for i in range(6):
    if women[i] > K:
        room += women[i] // 2 + women[i] % 2
    elif women[i] > 0:
        room += 1

    if men[i] > K:
        room += men[i] // 2 + men[i] % 2
    elif men[i] > 0:
        room += 1

print(room)
