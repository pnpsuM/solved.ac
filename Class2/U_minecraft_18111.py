import sys
import heapq as h

TIME_CRASH = 2
TIME_SET = 1
time = 0

minij = 987987987
min_time = 987987987

row, col, B = tuple(map(int, sys.stdin.readline().rstrip().split()))
block_map = []
for i in range(row):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    block_map.append(line)
    minij = min(minij, min(line))
print(block_map, minij)
