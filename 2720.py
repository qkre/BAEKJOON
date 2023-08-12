T = int(input())

for i in range(T):
    C = int(input())
    quarter = C // 25
    C -= quarter * 25
    dime = C // 10
    C -= dime * 10
    nickel = C // 5
    C -= nickel * 5
    penny = C // 1
    print(f"{quarter} {dime} {nickel} {penny}")
