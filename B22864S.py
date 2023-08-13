A, B, C, M = map(int, input().split())

hour = 0
HP = M
work = 0
while hour < 24:
    if HP - A >= 0:
        hour += 1
        work += B
        HP -= A
    else:
        if HP + C <= M:
            HP += C
        else:
            HP = M
        hour += 1

print(work)
