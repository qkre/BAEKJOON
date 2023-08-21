N, M = map(int, input().split())
name_list = []
twice = {}
for _ in range(N + M):
    name_list.append(input())

name_list.sort()

for name in name_list:
    try:
        twice[name] += 1
    except:
        twice[name] = 1

name_list = sorted(list(set(name_list)))
result = []
for name in name_list:
    if twice[name] == 2:
        result.append(name)

print(len(result))
for name in result:
    print(name)
