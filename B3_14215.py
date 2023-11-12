arr = list(map(int, input().split()))

arr.sort()

while True:
    if arr[-1] < arr[0] + arr[1]:
        print(sum(arr))
        break
    else:
        arr[-1] -= 1