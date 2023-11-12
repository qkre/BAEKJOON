while True:
    arr = list(map(int, input().split()))

    if sum(arr) == 0:
        break

    arr.sort()

    if arr[-1] >= sum(arr[:-1]):
        print("Invalid")
        continue

    if arr.count(arr[0]) == 3:
        print("Equilateral")
        continue
    elif arr.count(arr[0]) == 2 or arr.count(arr[1]) == 2:
        print("Isosceles")
        continue
    else:
        print("Scalene")