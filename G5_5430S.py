from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())

for _ in range(T):
    P = list(input().rstrip())
    N = int(input())
    arr = list(input().rstrip()[1:-1].split(","))

    if N > 0:
        nums = deque(arr)

        try:
            reverse = 0
            for i in P:
                if i == "R":
                    reverse += 1
                elif i == "D":
                    if reverse % 2 == 0:
                        nums.popleft()
                    else:
                        nums.pop()

            if reverse % 2 == 0:
                print("[" + ",".join(nums) + "]")
            else:
                nums.reverse()
                print("[" + ",".join(nums) + "]")

        except:
            print("error")
    else:
        if "D" in P:
            print("error")
        else:
            print("[]")
