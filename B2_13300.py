N, K = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))

W, M = [[0] for _ in range(6)], [[0] for _ in range(6)]

for i in arr:
    gender, grade = i[0], i[1]

    if gender == 0:
        if W[grade-1][-1] == K:
            W[grade-1].append(1)
        else:
            W[grade-1][-1] += 1

    else:
        if M[grade-1][-1] == K:
            M[grade-1].append(1)
        else:
            M[grade-1][-1] += 1

ans = 0

for i in W:
    for j in i:
        if j != 0:
            ans += 1

for i in M:
    for j in i:
        if j != 0:
            ans += 1

print(ans)