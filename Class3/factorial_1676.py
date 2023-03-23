import sys
from math import factorial

N = int(sys.stdin.readline())
string = str(factorial(N))
string = reversed(string)
cnt = 0
for ch in string:
    if ch == '0':
        cnt += 1
    else:
        break
print(cnt)