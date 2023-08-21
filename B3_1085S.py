x, y, w, h = map(int, input().split())

top_x = w - x
top_h = h - y

print(min(x, y, top_h, top_x))
