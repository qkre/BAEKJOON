from sys import stdin
import copy

N = int(input())
ans = "1"*N


def is_valid(ans, N):
    for i in range(N - 1):
        if ans[i] == ans[i + 1]:
            return False

    for i in range(N):
        for j in range(i + 1, N):
            if j * 2 - i >= N:
                continue
            if ans[i:j] == ans[j : j * 2 - i]:
                return False


while ans != "3"*N:
    num_ans = int(ans)
    if 