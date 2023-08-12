import sys
import itertools

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

stay = []
goal = []

for i in numbers:
    if not goal:
        if i != 1:
            stay.append(i)
        else:
            goal.append(i)
    else:
        if not stay:
            if goal[-1] + 1 != i:
                stay.append(i)
            else:
                goal.append(i)
        else:
            while goal[-1] + 1 == stay[-1]:
                goal.append(stay.pop())
                if not stay:
                    break
            if goal[-1] + 1 != i:
                stay.append(i)
            else:
                goal.append(i)

while stay:
    goal.append(stay.pop())

print("Nice" if goal == sorted(numbers) else "Sad")
