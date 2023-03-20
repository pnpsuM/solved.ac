import sys

N = int(sys.stdin.readline())
visited = {}

for loop in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    