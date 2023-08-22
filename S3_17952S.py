# 과제는 끝나지 않아!
# 구현, 자료구조, 스택
from sys import stdin

input = stdin.readline

N = int(input())

assignment = []
timer = []
score = 0
for _ in range(N):
    command = list(map(int, input().split()))
    try:
        if command[0] == 0:
            timer[-1] -= 1
            if timer[-1] == 0:
                score += assignment.pop()
                timer.pop()
        else:
            if command[2] == 1:
                score += command[1]
            else:
                assignment.append(command[1])
                timer.append(command[2] - 1)
    except:
        continue

print(score)
