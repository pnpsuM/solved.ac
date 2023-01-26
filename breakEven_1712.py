import sys

A, B, C = tuple(map(int, sys.stdin.readline().rstrip().split()))
if (C - B):
    BEP = A // (C - B) + 1
else:
    print('-1')
    exit()
if BEP > 0:
    print(BEP)
else:
    print('-1')