import sys

# 0 - elevator, 1 ~ W - room
loop = int(sys.stdin.readline())
for i in range(loop):
    H, W, N = tuple(map(int, sys.stdin.readline().split()))
    
    h = str((N - 1) % H + 1)
    w = (N - 1) // H + 1
    if w < 10:
        w = '0' + str(w)
    else:
        w = str(w)
    print(h + w)