import sys

memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1

loop = int(sys.stdin.readline())
N = int(sys.stdin.readline())
for j in loop:
    for i in range(3, N):
        memo[i] = memo[i-1] + memo[i-2]