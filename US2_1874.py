from sys import stdin

input = stdin.readline

N = int(input())

checked = list(False for _ in range(N))
stack = [1]
cmd = ["+"]
wannabe = list(int(input()) for _ in range(N))


cursor = 2
for i in range(N):
    while wannabe[i] != stack[-1]:
        if cursor > N:
            print("NO")
            quit()

        stack.append(cursor)
        cursor += 1
        cmd.append("+")

    cmd.append("-")
    stack.pop()

    if len(stack) == 0:
        stack.append(cursor)
        cursor += 1
        cmd.append("+")

if len(stack) == 0:
    for i in cmd:
        print(i)
