import sys
import heapq as h

N = int(sys.stdin.readline())
heap = []

for loop in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    h.heappush(heap, (start, end))

length = 0
cnt = 0
while len(heap):
    st, ed = h.heappop(heap)
    if ed < length:
        length = ed
    elif st >= length:
        cnt += 1
        length = ed
print(cnt)