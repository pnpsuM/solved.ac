import heapq as h
import sys

num = int(sys.stdin.readline())
names = []
for i in range(num):
    age, name = sys.stdin.readline().rstrip().split()
    h.heappush(names, (int(age), i, name))
while names:
    age, _, name = h.heappop(names)
    print(age, name)