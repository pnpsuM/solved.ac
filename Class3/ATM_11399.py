import sys
import heapq as h

num = int(sys.stdin.readline())
minutes = list(map(int, sys.stdin.readline().split()))

h.heapify(minutes)
sum = 0
total = 0
while(minutes):
    sum += h.heappop(minutes)
    total += sum
print(total)