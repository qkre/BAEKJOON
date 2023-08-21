arr = [[]] * 5

for i in range(5):
    arr[i] = input()

strLength = 0

maxlen = 0

for i in arr:
    maxlen = max(maxlen, len(i))
    strLength += len(i)

result = ""
col = 0
while len(result) != strLength:
    for i in range(5):
        try:
            result += arr[i][col]
        except:
            continue

    col += 1

print(result)
