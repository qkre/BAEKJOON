N = int(input())

d = {}

arr = list(list(input()) for _ in range(N))

for S in arr:

    for i in range(len(S), 0, -1):
        if S[len(S) - i] not in d:
            d[S[len(S) - i]] = 10 ** (i - 1)
        else:
            d[S[len(S) - i]] += 10 ** (i - 1)

d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

keys = list(d.keys())
num_d = {}

for i in range(len(keys)):
    num_d[keys[i]] = 9 - i


ans = 0

for S in arr:
    for i in range(len(S)):
        S[i] = num_d[S[i]]

    ans += int(''.join(list(map(str, S))))

print(ans)
