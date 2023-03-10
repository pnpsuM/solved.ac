import heapq as h
import sys

loop = int(sys.stdin.readline())
heap = []

def action_0(heap):
    if len(heap):
        return -h.heappop(heap)
    else:
        return 0

for iter in range(loop):
    inputs = int(sys.stdin.readline())
    if inputs == 0:
            print(action_0(heap))
    else:
        h.heappush(heap, -inputs)