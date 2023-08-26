# 시간 관리
# 그리디 알고리즘, 정렬

from sys import stdin

input = stdin.readline

N = int(input())
time_table = list(list(map(int, input().split())) for _ in range(N))
time_table.sort(key=lambda x: x[1])

time = 0
global valid_check
valid_check = True


def do(time, index, N, time_table):
    global valid_check
    if index == N:
        if time <= 1000000:
            valid_check = True
        else:
            valid_check = True
    elif time + time_table[index][0] <= time_table[index][1]:
        do(time + time_table[index][0], index + 1, N, time_table)
    else:
        tmp = time_table[index]
        time_table[index] = time_table[index + 1]
        time_table[index + 1] = tmp
        do(time, index, N, time_table)


for i in range(1000000):
    try:
        do(i, 0, N, time_table)
    except:
        if i == 0:
            print(-1)
        else:
            print(i - 1)
        break
