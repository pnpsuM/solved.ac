import sys

seek, hide = tuple(map(int, sys.stdin.readline().split()))
memo = {}
time = 0
memo[seek] = time

while True:
    flag = 0
    loc = seek + 1
    flag = 1 if loc == hide else 0
    try: memo[loc] = min(memo[loc], memo[seek] + 1)
    except: memo[loc] = memo[seek] + 1

    loc = seek - 1
    flag = 1 if loc == hide else 0
    try: memo[loc] = min(memo[loc], memo[seek] + 1)
    except: memo[loc] = memo[seek] + 1
    
    loc = seek * 2
    flag = 1 if loc == hide else 0
    try: memo[loc] = min(memo[loc], memo[seek] + 1)
    except: memo[loc] = memo[seek] + 1

    if flag == 1:
        break
print(memo[hide])