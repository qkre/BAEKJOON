import sys

input = sys.stdin.readline

N = int(input())

arr = list(list(input().rstrip().split(".")) for _ in range(N))

arr.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

start = arr[0]
end = arr[-1]

needs = 0
for i in range(4):
    tmp = (end[i] - start[i])**