import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = list(map(int, input().split()))
    if len(command) == 1:
        if command[0] == 2:
            try:
                print(stack.pop())
            except:
                print(-1)
        elif command[0] == 3:
            print(len(stack))
        elif command[0] == 4:
            print(1 if not stack else 0)
        elif command[0] == 5:
            try:
                print(stack[0])
            except:
                print(-1)
    else:
        stack.append(command[1])
