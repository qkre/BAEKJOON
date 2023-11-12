N = int(input())

arr = list(list(map(int, input().split())) for _ in range(N))

arr.sort(key=lambda x: x[0])

if len(arr) < 2:
    print(0)
else:
    width = arr[-1][0] - arr[0][0]
    arr.sort(key= lambda x: x[1])
    height = arr[-1][1] - arr[0][1]
    print(width * height)