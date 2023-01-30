import sys
import heapq as h

num = int(sys.stdin.readline())
coord = []

for i in range(num):
    x, y = tuple(map(int, sys.stdin.readline().rstrip().split()))
    h.heappush(coord, (x, y))

while coord:
    x, y = h.heappop(coord)
    print(x, y)