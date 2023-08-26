# 다이어트

from sys import stdin
import math

input = stdin.readline

G = int(input())
num = [i for i in range(1, 100001)]


def binary_search(i, target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if i**2 - data[mid] ** 2 == target:
            return i
        elif i**2 - data[mid] ** 2 > target:
            start = mid + 1
        else:
            end = mid - 1

    return None


printed = False
for i in range(1, 100001):
    ans = binary_search(i, G, num)
    if ans != None:
        printed = True
        print(ans)

if not printed:
    print(-1)
