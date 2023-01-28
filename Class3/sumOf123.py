import sys

len = int(sys.stdin.readline())

for loop in range(len):
    num = int(sys.stdin.readline())
    memo = [0] * (num + 1)
    
    memo[0] = 1
    for i in range(0, num + 1):
        if i + 3 <= num:
            memo[i + 3] += memo[i]
        if i + 2 <= num:
            memo[i + 2] += memo[i]
        if i + 1 <= num:
            memo[i + 1] += memo[i]
    print(memo[num])