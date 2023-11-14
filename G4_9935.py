S = list(input())
target = list(input())
temp = []
while len(S) > 0:
    temp.append(S.pop())

    if len(temp) >= len(target):
        same = True
        for i in range(len(target)):
            if temp[-1 - i] != target[i]:
                same = False
                break

        if same:
            for _ in range(len(target)):
                temp.pop()

if len(temp) > 0:
    print(''.join(list(reversed(temp))))
else:
    print("FRULA")
