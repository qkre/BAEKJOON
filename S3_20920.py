from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) >= M:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for _ in sorted_dict:
    print(_[0])