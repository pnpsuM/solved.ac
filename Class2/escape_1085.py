from sys import stdin

x, y, w, h = tuple(map(int, stdin.readline().split()))

minx = min(x, w - x)
miny = min(y, h - y)

print(min(minx, miny))