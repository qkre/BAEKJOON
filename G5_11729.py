import sys
import copy

sys.setrecursionlimit(10**5)


N = int(input())

first = list(i for i in range(N, 0, -1))
second = []
third = []

min_move = 987654321
move_arr = [[0, 0]]

origin = copy.deepcopy(first)


def dfs(move):
    if third == origin:
        min_move = min(min_move, len(move))
        move_arr = copy.deepcopy(move)
        return

    if len(first) > 0:
        if move[-1] != [2, 1]:
            if len(second) == 0 or first[-1] < second[-1]:
                second.append(first.pop())
                move.append([1, 2])
                dfs(move)
                move.pop()
                first.append(second.pop())

        if move[-1] != [3, 1]:
            if len(third) == 0 or first[-1] < third[-1]:
                third.append(first.pop())
                move.append([1, 3])
                dfs(move)
                move.pop()
                first.append(third.pop())

    if len(second) > 0:
        if move[-1] != [3, 2]:
            if len(third) == 0 or second[-1] < third[-1]:
                third.append(second.pop())
                move.append([2, 3])
                dfs(move)
                move.pop()
                second.append(third.pop())

        if move[-1] != [1, 2]:
            if len(first) == 0 or second[-1] < first[-1]:
                first.append(second.pop())
                move.append([2, 1])
                dfs(move)
                move.pop()
                second.append(first.pop())

    if len(third) > 0:
        if move[-1] != [2, 3]:
            if len(second) == 0 or third[-1] < second[-1]:
                second.append(third.pop())
                move.append([3, 2])
                dfs(move)
                move.pop()
                third.append(second.pop())

        if move[-1] != [1, 3]:
            if len(first) == 0 or third[-1] < first[-1]:
                first.append(third.pop())
                move.append([3, 1])
                dfs(move)
                move.pop()
                third.append(first.pop())


dfs(move_arr)
