import sys
import math

N, K = tuple(map(int, sys.stdin.readline().split()))

memo = [0] * (N + 1)
memo[0] = 1

for i in range(1, N + 1):
    memo[i] = math.factorial(N) / (math.factorial(i) * math.factorial(N - i))
    
print(int(memo[K]))