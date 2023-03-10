import sys

num = int(sys.stdin.readline())
memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 3

for i in range(4, num + 1):
    memo[i] = memo[i-1] + memo[i-2]
    
print(memo[num] % 10007)